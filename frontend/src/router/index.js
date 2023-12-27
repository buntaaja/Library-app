import Vue from "vue";
import VueRouter from "vue-router";
import Shark from "../components/Shark";
import ListOfBooks from "../components/ListOfBooks";

Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "Shark",
    component: Shark,
  },
  {
    path: "/books",
    name: "Books",
    component: ListOfBooks,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
