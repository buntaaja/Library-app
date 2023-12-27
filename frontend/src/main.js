import Vue from "vue";
import App from "./App.vue";
import router from "./router";
// Install bootstrap first
import "bootstrap/dist/css/bootstrap.css";
// Importing bootstrapvue library
import BootstrapVue from "bootstrap-vue";

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
