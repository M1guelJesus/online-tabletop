import { createStore } from "vuex";

const connectionStore = createStore({
	state() {
		return {
			ip: import.meta.env.VITE_API_IP || "127.0.0.1",
			port: import.meta.env.VITE_API_PORT || "8000",
			token: import.meta.env.VITE_API_TOKEN || "test",
		};
	},
	mutations: {
		setIp(state, ip) {
			state.ip = ip;
		},
		setPort(state, port) {
			state.port = port;
		},
		setToken(state, token) {
			state.token = token;
		},
	},
});

export default connectionStore;
