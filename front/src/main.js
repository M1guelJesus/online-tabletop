import "./index.css";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import connectionStore from "./stores/connection";

const app = createApp(App).use(connectionStore);

app.use(router).mount("#app");
