<script setup>
import MyInput from "@/components/inputs/myInput.vue";
import MyButton from "@/components/myButton.vue";
import router from "@/router";
import connectionStore from "@/stores/connection";
import { useVuelidate } from "@vuelidate/core";
import { between, ipAddress, minLength, numeric, required } from "@vuelidate/validators";
import { ref } from "vue";

const { push } = router;
const state = ref({
	ip: connectionStore.state.ip,
	port: connectionStore.state.port,
	token: connectionStore.state.token,
});
const rules = {
	ip: {
		required,
		ipAddress,
	},
	port: {
		required,
		numeric,
		between: between(1, 65535),
	},
	token: {
		required,
		minLength: minLength(3),
	},
};
const v$ = useVuelidate(rules, state);
const buttonState = ref({
	loading: false,
	check: false,
	x: false,
});

async function saveSettings() {
	buttonState.value.x = false;
	buttonState.value.check = false;
	buttonState.value.loading = true;
	await new Promise((r) => setTimeout(r, 1000));
	const isFormCorrect = await v$.value.$validate();
	if (!isFormCorrect) {
		buttonState.value.loading = false;
		buttonState.value.x = true;
		return;
	}

	connectionStore.commit("setIp", state.value.ip);
	connectionStore.commit("setPort", state.value.port);
	connectionStore.commit("setToken", state.value.token);
	buttonState.value.x = false;
	buttonState.value.check = true;
	buttonState.value.loading = false;
	await new Promise((r) => setTimeout(r, 500));
	push({ name: "Board" });
}
</script>

<template>
	<main class="">
		<form @submit.prevent="saveSettings" class="space-y-4 max-w-md mx-auto mt-12">
			<MyInput
				type="text"
				name="ip"
				mask="#00.#00.#00.#00"
				mask-tokens="0:[0-9]:optional"
				id="ip-input"
				label="IP Address of server (X.X.X.X)"
				:optionSelected="state.ip || ''"
				:rules="rules.ip"
				:errors="(v$.ip.$errors || []).map((a) => a.$message)"
				@value-changed="(v) => (state.ip = v)" />
			<MyInput
				type="text"
				name="port"
				id="port-input"
				label="Port of server"
				:optionSelected="state.port || ''"
				:errors="(v$.port.$errors || []).map((a) => a.$message)"
				@value-changed="(v) => (state.port = v)" />
			<MyInput
				type="text"
				name="token"
				id="token-input"
				label="Name of the room"
				:optionSelected="state.token || ''"
				:errors="(v$.token.$errors || []).map((a) => a.$message)"
				@value-changed="(v) => (state.token = v)" />
			<MyButton
				id="connection-settings-button"
				type="submit"
				class="rounded-full"
				:loading="buttonState.loading"
				:show-check="buttonState.check"
				:show-x="buttonState.x"
				:outline="false"
				:defaultColor="true">
				<p class="text-center mx-auto">Continue</p>
			</MyButton>
		</form>
	</main>
</template>
