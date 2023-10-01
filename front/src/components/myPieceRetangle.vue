<script setup>
import { onMounted, ref } from "vue";

const emit = defineEmits(["pieceMoved", "delete", "rotated"]);

const props = defineProps({
	id: {
		type: String,
		required: true,
	},
	width: {
		type: Number,
		required: true,
	},
	height: {
		type: Number,
		required: true,
	},
	color: {
		type: String,
		required: true,
	},
	name: {
		type: String,
		required: true,
	},
	angle: {
		type: Number,
		required: true,
	},
	x: {
		type: Number,
		required: true,
	},
	y: {
		type: Number,
		required: true,
	},
});
let piece = ref(null);
let rotateP = ref(null);
let offsetX = ref(props.x);
let offsetY = ref(props.y);
let rotateAngle = ref(props.angle);
let rotating = ref(null);

onMounted(() => {
	piece.value.style.top = `${props.y}px`;
	piece.value.style.left = `${props.x}px`;
});

function startDrag(e) {
	offsetY.value = e.clientY - parseInt(piece.value.style.top);
	offsetX.value = e.clientX - parseInt(piece.value.style.left);
}

function endDrag(e) {
	emit("pieceMoved", {
		x: e.clientX - offsetX.value,
		y: e.clientY - offsetY.value,
		id: props.id,
	});
}

function handleKeyPressDown(e) {
	if (e.code == "KeyR") {
		if (e.repeat) return;
		rotateAngle.value += 5;
		rotateP.value.style.opacity = 100;
		rotating.value = setInterval(() => {
			rotateAngle.value += 5;
			if (rotateAngle.value >= 360) {
				rotateAngle.value = 0;
			}
		}, 100);
	}
}

function handleKeyPressUp(e) {
	if (e.code == "KeyD") emit("delete", props.id);
	if (e.code == "KeyR") {
		clearInterval(rotating.value);
		rotating.value = null;
		setTimeout(() => {
			rotateP.value.style.opacity = 0;
		}, 500);
		emit("rotated", { angle: rotateAngle.value, id: props.id });
	}
}
</script>
<template>
	<div
		ref="piece"
		:id="props.id"
		class="cursor-pointer absolute group w-full h-full"
		:style="`top: ${props.y}px; left: ${props.x}px; width: ${props.width}px; height: ${props.height}px; color: ${props.color}; rotate: ${rotateAngle}deg`"
		draggable="true"
		tabindex="0"
		@dragstart="(e) => startDrag(e)"
		@dragend="(e) => endDrag(e)"
		@keydown="(e) => handleKeyPressDown(e)"
		@keyup="(e) => handleKeyPressUp(e)">
		<p class="absolute m-auto text-black">
			{{ props.name }}
		</p>
		<p
			ref="rotateP"
			class="absolute left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 text-black z-50 opacity-0 transition-all duration-200"
			style="opacity: 0">
			{{ `${rotateAngle}º` }}
		</p>
		<svg height="100%" width="100%">
			<!-- Retangle -->
			<polygon
				:points="`0,0 ${props.width},0 ${props.width},${props.height} 0,${props.height}`"
				stroke="currentColor"
				fill="currentColor" />
		</svg>
	</div>
</template>
