<template>
  <div id="app">
    <NavBar />
    <router-view/>
  </div>
</template>


<script>
// @ is an alias to /src
import NavBarVue from "@/components/NavBar.vue";
import NavBar from "./components/NavBar.vue";
export default{
  components: {
    NavBarVue,
    NavBar
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.main {
  padding-top: 5em;
}

</style>
