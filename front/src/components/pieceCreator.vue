<script setup>
import { ref } from "vue";
import MyInput from "./inputs/myInput.vue";
import MySelectInverted from "./inputs/mySelectInverted.vue";
import MyButton from "./myButton.vue";
import MyColorPicker from "./inputs/myColorPicker.vue";
import InfoBoard from "./infoBoard.vue";

const emit = defineEmits(["newPiece"]);
const objSize = [
	{ id: "custom", name: "Custom" },
	{ id: "tiny", name: "Tiny (2.5 ft)" },
	{ id: "small", name: "Small (5 ft)" },
	{ id: "medium", name: "Medium (5 ft)" },
	{ id: "large", name: "Large (10 ft)" },
	{ id: "huge", name: "Huge (15 ft)" },
	{ id: "gargantuan", name: "Gargantuan (20 ft)" },
];

let name = ref("");
let size = ref("");
let width = ref("");
let height = ref("");
let color = ref("#ff0000");
let error = ref({
	name: "",
	size: "",
	width: "",
	height: "",
});

function createComponent() {
	name.value = name.value.trim();
	error.value.name = "";
	error.value.size = "";
	error.value.width = "";
	error.value.height = "";
	// if (!name.value) {
	// 	error.value.name = "Must have a name";
	// 	return;
	// }

	let widthSent = 40;
	let heightSent = 40;
	if (!size.value) {
		error.value.size = "Must have a size";
		return;
	}
	if (size.value === "custom") {
		if (!width.value) {
			error.value.width = "Must have a width";
			return;
		}
		if (!height.value) {
			error.value.height = "Must have a height";
			return;
		}
		widthSent = width.value * 45;
		heightSent = height.value * 45;
	} else {
		switch (size.value) {
			case "tiny":
				widthSent = 16;
				heightSent = 16;
				break;
			case "small":
				widthSent = 36;
				heightSent = 36;
				break;
			case "medium":
				widthSent = 40;
				heightSent = 40;
				break;
			case "large":
				widthSent = 64;
				heightSent = 64;
				break;
			case "huge":
				widthSent = 100;
				heightSent = 100;
				break;
			case "gargantuan":
				widthSent = 200;
				heightSent = 200;
				break;
			default:
				break;
		}
	}
	emit("newPiece", {
		name: name.value,
		width: widthSent,
		height: heightSent,
		color: color.value,
		angle: 0,
		id: `${name.value}.${Math.floor(Math.random() * 10e8)}`,
	});
}
</script>

<template>
	<div class="fixed bottom-0 bg-white w-full px-8 py-4">
		<form
			@submit.prevent="createComponent"
			class="w-full grid grid-cols-5 px-4 py-2 gap-x-4 border-2 border-black rounded-md">
			<MyInput
				type="text"
				name="name"
				id="name"
				label="Name"
				optionSelected=""
				:error="error.name"
				@value-changed="(v) => (name = v)" />
			<div>
				<MySelectInverted
					:options="objSize"
					name="size"
					id="size"
					label="Size"
					optionSelected=""
					:error="error.size"
					@value-changed="(v) => (size = v)" />
				<MyInput
					v-if="size === 'custom'"
					type="text"
					name="width"
					id="width"
					label="Width (hexes)"
					optionSelected=""
					:error="error.width"
					@value-changed="(v) => (width = v)" />
				<MyInput
					v-if="size === 'custom'"
					type="text"
					name="height"
					id="height"
					label="Height (hexes)"
					optionSelected=""
					:error="error.height"
					@value-changed="(v) => (height = v)" />
			</div>
			<MyColorPicker
				name="color"
				id="color"
				label="Color"
				:optionSelected="color"
				:error="error.name"
				@value-changed="(v) => (color = v)" />
			<div class="mt-auto">
				<MyButton
					id="button"
					type="submit"
					class="rounded-full"
					:loading="false"
					:show-check="false"
					:show-x="false"
					:outline="true"
					:defaultColor="true">
					<p class="text-center mx-auto">Submit</p>
				</MyButton>
			</div>
			<InfoBoard />
		</form>
	</div>
</template>
