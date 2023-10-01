import axios from "axios";

export { API_URL, api };
const API_URL =
	import.meta.env.VITE_API_API_URL == undefined
		? "http://37.189.106.39:8000/"
		: import.meta.env.VITE_API_API_URL;

const HEADERS = {
	"Content-Type": "application/json",
};

const TIMEOUT = 70000;

const api = axios.create({
	baseURL: API_URL,
	headers: HEADERS,
	timeout: TIMEOUT,
});

api.interceptors.response.use(
	(response) => {
		return response;
	},
	function (error) {
		return Promise.reject(error);
	}
);
