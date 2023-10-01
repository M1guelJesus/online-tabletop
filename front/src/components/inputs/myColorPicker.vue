<script setup>
import { ExclamationCircleIcon } from "@heroicons/vue/24/solid";
import { ref, watch } from "vue";
import { vMaska } from "maska";

const props = defineProps({
	name: {
		type: String,
		required: true,
	},
	id: {
		type: String,
		required: true,
	},
	label: {
		type: String,
		required: true,
	},
	optionSelected: {
		type: String,
		required: true,
	},
	readonly: {
		type: Boolean,
		required: false,
		default: false,
	},
});

let state = ref(props.optionSelected);
const emit = defineEmits(["valueChanged"]);

watch(
	() => state.value,
	(after) => {
		emit("valueChanged", after);
	}
);

watch(
	() => props.optionSelected,
	(after) => {
		state.value = after;
	}
);
</script>

<template>
	<div :id="`input-${props.id}`" :class="[props.readonly && 'opacity-50']">
		<label :id="`label-${props.id}`" :for="props.name">{{ label }}</label>
		<div class="relative mt-1 rounded-md shadow-sm px-2">
			<input
				:id="props.id"
				v-model="state"
				type="color"
				:name="props.name"
				class="w-full rounded-md border py-0.5 px-2"
				:disabled="props.readonly" />
		</div>
	</div>
</template>
