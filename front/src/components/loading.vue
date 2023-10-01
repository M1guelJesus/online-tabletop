<script setup>
const props = defineProps({
	size: {
		type: Number,
		required: false,
		default: 10,
	},
});
</script>

<template>
	<svg class="animate-spin mx-auto" :style="`width: ${props.size}rem`" viewBox="0 0 50 50">
		<path
			fill="currentColor"
			d="M25.251,6.461c-10.318,0-18.683,8.365-18.683,18.683h4.068c0-8.071,6.543-14.615,14.615-14.615V6.461z"></path>
	</svg>
</template>
