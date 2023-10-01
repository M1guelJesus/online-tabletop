<script setup>
import Loading from "@/components/loading.vue";
import MyPieceRetangle from "@/components/myPieceRetangle.vue";
import PieceCreator from "@/components/pieceCreator.vue";
import connectionStore from "@/stores/connection";
import { ref } from "vue";

const socket = new WebSocket(
	`ws://${connectionStore.state.ip}:${connectionStore.state.port}/ws?token=${connectionStore.state.token}`
);
const board = ref(null);
const pieces = ref([]);
const loading = ref(true);

socket.onopen = () => {
	socket.send(JSON.stringify({ socketType: "loadExisting" }));
};

socket.onmessage = async (e) => {
	const data = JSON.parse(e.data);
	if (data.socketType === "create") {
		createPiece(data.name, data.width, data.height, data.color, data.angle, data.id);
	} else if (data.socketType === "move") {
		movePiece(data.x, data.y, data.id);
	} else if (data.socketType === "rotate") {
		rotatePiece(data.angle, data.id);
	} else if (data.socketType === "delete") {
		deletePiece(data.id);
	} else if (data.socketType == "loadExisting") {
		broadcastExisting();
	} else if (loading.value && data.socketType == "reload") {
		pieces.value = data.pieces;
		loading.value = false;
	}
};

function movePiece(x, y, id) {
	const el = document.getElementById(id);
	if (el != null) {
		let pieceIndex = pieces.value.findIndex((a) => a.id == id);
		if (pieceIndex !== -1) {
			pieces.value[pieceIndex].x = x;
			pieces.value[pieceIndex].y = y;
			el.style.left = `${x}px`;
			el.style.top = `${y}px`;
		}
	}
}

function rotatePiece(angle, id) {
	const el = document.getElementById(id);
	if (el != null) {
		let pieceIndex = pieces.value.findIndex((a) => a.id == id);
		if (pieceIndex !== -1) {
			pieces.value[pieceIndex].angle = angle;
			el.style.rotate = `${angle}deg`;
		}
	}
}

function createPiece(name, width, height, color, angle, id) {
	pieces.value.push({
		id: id,
		name: name,
		width: width,
		height: height,
		color: color,
		angle: angle,
		x: 10,
		y: 10,
	});
}

function broadcastNewPiece(name, width, height, color, angle, id) {
	socket.send(
		JSON.stringify({
			socketType: "create",
			name: name,
			width: width,
			height: height,
			color: color,
			angle: angle,
			id: id,
		})
	);
}

function broadcastMove(x, y, id) {
	socket.send(JSON.stringify({ socketType: "move", x: x, y: y, id: id }));
}

function broadcastExisting() {
	socket.send(JSON.stringify({ socketType: "reload", pieces: pieces.value }));
}

function broadcastRotate(angle, id) {
	socket.send(JSON.stringify({ socketType: "rotate", angle: angle, id: id }));
}

function broadcastDelete(id) {
	socket.send(JSON.stringify({ socketType: "delete", id: id }));
}

function deletePiece(id) {
	const pieceIndex = pieces.value.findIndex((a) => a.id == id);
	if (pieceIndex === -1) {
		return;
	}
	pieces.value.splice(pieceIndex, 1);
}
</script>

<template>
	<main class="">
		<Loading v-if="loading" :size="10" />
		<div v-else ref="board" class="absolute inset-0">
			<div class="absolute inset-0 w-[90%]"></div>
			<div
				class="w-[5000px] h-[5000px] absolute"
				style="background-image: url(public/hexGrid.png)"></div>
			<PieceCreator
				class=""
				@new-piece="
					(v) => broadcastNewPiece(v.name, v.width, v.height, v.color, v.angle, v.id)
				" />
			<MyPieceRetangle
				v-for="piece in pieces"
				:key="piece.id"
				:id="piece.id"
				:width="piece.width"
				:height="piece.height"
				:color="piece.color"
				:name="piece.name"
				:angle="piece.angle"
				:x="parseInt(piece.x)"
				:y="parseInt(piece.y)"
				@piece-moved="(v) => broadcastMove(v.x, v.y, v.id)"
				@rotated="(v) => broadcastRotate(v.angle, v.id)"
				@delete="(id) => broadcastDelete(id)" />
		</div>
	</main>
</template>
