<script setup>
import { CheckCircleIcon, XCircleIcon } from "@heroicons/vue/24/outline";

const props = defineProps({
	id: {
		required: true,
		type: String,
	},
	loading: {
		required: true,
		type: Boolean,
	},
	showCheck: {
		required: true,
		type: Boolean,
	},
	showX: {
		required: true,
		type: Boolean,
	},
	outline: {
		required: true,
		type: Boolean,
	},
	defaultColor: {
		required: true,
		type: Boolean,
	},
});

const emit = defineEmits(["buttonClick"]);
</script>

<template>
	<button
		:id="props.id"
		:class="[
			'border-2 w-full shadow-sm focus:outline-none select-none cursor-pointer focus:ring-2 focus:ring-offset-2 relative hover:-translate-y-0.5 py-2 px-4 rounded-md font-medium',
			props.showSpinningWheel || props.showCheck ? 'pointer-events-none opacity-50' : '',
			props.outline ? 'font-medium' : 'border-transparent hover:shadow-lg',
			props.defaultColor
				? props.outline
					? 'border-blue-600 text-blue-700 hover:bg-blue-300 hover:text-blue-800 focus:ring-blue-600 active:bg-blue-400'
					: 'text-white border-blue-500 hover:border-blue-700 active:border-blue-900 bg-blue-500 hover:bg-blue-600 active:bg-blue-700 focus:ring-blue-700'
				: '',
		]"
		@click="emit('buttonClick')">
		<svg v-if="props.loading" class="animate-spin w-6 h-6 mx-auto" viewBox="0 0 50 50">
			<path
				fill="currentColor"
				d="M25.251,6.461c-10.318,0-18.683,8.365-18.683,18.683h4.068c0-8.071,6.543-14.615,14.615-14.615V6.461z"></path>
		</svg>
		<div v-else>
			<div class="inline-flex justify-between w-full">
				<slot></slot>
			</div>
		</div>
		<CheckCircleIcon
			v-show="props.showCheck"
			style="width: 24px"
			class="absolute right-0 mr-3 top-1/2 -translate-y-1/2" />
		<XCircleIcon
			v-show="props.showX"
			style="width: 24px"
			class="absolute right-0 mr-3 top-1/2 -translate-y-1/2" />
	</button>
</template>
