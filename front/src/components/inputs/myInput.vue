<script setup>
import { ExclamationCircleIcon } from "@heroicons/vue/24/solid";
import { vMaska } from "maska";
import { ref, watch } from "vue";

const props = defineProps({
	type: {
		type: String,
		required: true,
		validator(value) {
			// The type must match one of these strings
			return ["text", "password", "tel", "number"].includes(value);
		},
	},
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
	errors: {
		type: Array,
		required: false,
		default: [],
	},
	readonly: {
		type: Boolean,
		required: false,
		default: false,
	},
	mask: {
		type: String,
		required: false,
		default: "",
	},
	maskTokens: {
		type: String,
		required: false,
		default: "",
	},
	rules: {
		type: Object,
		required: false,
		default: {},
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
		<div class="relative mt-1 rounded-md shadow-sm">
			<input
				v-maska
				:data-maska="props.mask"
				:data-maska-tokens="props.maskTokens"
				:id="props.id"
				v-model="state"
				:type="props.type"
				:name="props.name"
				:class="[
					'w-full rounded-md pr-10 pl-2 border py-0.5',
					props.errors == ''
						? [
								'shadow-sm focus:border-indigo-500 focus:ring-indigo-500 border-gray-300',
						  ]
						: 'border-red-300 text-red-900 placeholder-red-300 focus:border-red-500 focus:outline-none focus:ring-red-500',
				]"
				:placeholder="props.placeholder"
				:aria-invalid="!props.errors"
				:disabled="props.readonly"
				:aria-describedby="`${props.name}-error`" />

			<div
				:id="`errorsymbol-${props.id}`"
				v-if="!props.errors"
				class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3">
				<ExclamationCircleIcon class="h-5 w-5 text-red-500" aria-hidden="true" />
			</div>
		</div>
		<div
			v-if="props.errors.length"
			:id="`errormessage-${props.id}`"
			class="mt-2 text-sm text-red-600">
			<p v-for="error of props.errors">{{ error }}</p>
		</div>
	</div>
</template>
