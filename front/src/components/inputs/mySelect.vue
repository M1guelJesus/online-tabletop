<script setup>
import { ExclamationCircleIcon, CheckIcon, ChevronUpDownIcon } from "@heroicons/vue/24/solid";
import {
	Combobox,
	ComboboxButton,
	ComboboxInput,
	ComboboxOption,
	ComboboxOptions,
} from "@headlessui/vue";
import { computed, ref, watch } from "vue";

const props = defineProps({
	// Options syntax:
	// {
	//		name: "name",		text that will appear on the select and will be searchable
	//		id: "id"			value emited when the option is clicked
	// }
	options: {
		type: Array,
		required: true,
	},
	label: {
		type: String,
		required: true,
	},
	name: {
		type: String,
		required: true,
	},
	id: {
		type: String,
		required: true,
	},
	optionSelected: {
		type: String,
		required: false,
		default: "",
	},
	error: {
		type: String,
		required: false,
		default: "",
	},
	readonly: {
		type: Boolean,
		required: false,
		default: false,
	},
});

let state = ref(props.optionSelected);

let searchText = ref("");
const emit = defineEmits(["valueChanged"]);
let emitData = true;

watch(
	() => props.optionSelected,
	(after) => {
		emitData = false;
		state.value = after;
	}
);

watch(
	() => state.value,
	(after) => {
		if (emitData) {
			emit("valueChanged", after);
		} else {
			emitData = true;
		}
	}
);
const filteredOptions = computed(() =>
	searchText.value === ""
		? props.options
		: props.options.filter((option) => {
				return option.name.toLowerCase().includes(searchText.value.toLowerCase());
		  })
);
</script>

<template>
	<div :class="[props.readonly && 'opacity-50']">
		<Combobox v-model="state" class="w-full" as="div">
			<label class="block text-gray-700">
				{{ props.label }}
			</label>
			<div class="relative mt-1">
				<ComboboxInput
					:disabled="props.readonly"
					:class="[
						'w-full rounded-md border bg-white py-0.5 pl-2 pr-10 shadow-sm focus:outline-none focus:ring-1',
						error == ''
							? 'border-gray-300 focus:border-indigo-500 focus:ring-indigo-500'
							: 'border-red-300 text-red-900 focus:border-red-500 focus:ring-red-500',
					]"
					:display-value="() => props.options.find((a) => a.id == state)?.name"
					@change="(e) => (searchText = e.target.value)" />
				<ComboboxButton
					:disabled="props.readonly"
					class="absolute inset-y-0 right-0 flex items-center rounded-r-md px-2 focus:outline-none">
					<ChevronUpDownIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
					<ExclamationCircleIcon
						v-if="error != ''"
						class="h-5 w-5 text-red-500"
						aria-hidden="true" />
				</ComboboxButton>

				<ComboboxOptions
					v-if="filteredOptions.length > 0"
					class="absolute z-50 max-h-60 bottom-8 w-full overflow-auto rounded-md bg-white py-0.5 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
					<ComboboxOption
						v-for="option in filteredOptions"
						:key="option.id"
						v-slot="{ active, selected }"
						:value="option.id"
						as="template">
						<li
							:class="[
								'relative cursor-default select-none py-2 pl-8 pr-4',
								active ? 'bg-indigo-600 text-white' : 'text-gray-900',
							]">
							<span :class="['block truncate', selected && 'font-semibold']">
								{{ option.name }}
							</span>

							<span
								v-if="option.id == state"
								:class="[
									'absolute inset-y-0 left-0 flex items-center pl-1.5',
									active ? 'text-white' : 'text-indigo-600',
								]">
								<CheckIcon class="h-5 w-5" aria-hidden="true" />
							</span>
						</li>
					</ComboboxOption>
				</ComboboxOptions>
			</div>
			<p
				v-if="error != ''"
				:id="`errormessage-${props.id}`"
				class="mt-2 text-sm text-red-600">
				{{ error }}
			</p>
		</Combobox>
	</div>
</template>
