<template>
  <div class="container">
    <h1>Which pizza are you ?</h1>
    <Input />
  </div>
</template>
<style>
@font-face {
  font-family: "Pizzat";
  src: url("./assets/Pizzat.ttf") format("truetype");
}

h1 {
  font-size: 5rem;
}

html {
  font-family: "Pizzat", sans-serif;
  background-image: url("./assets/background.jpg");
}

.container {
  background-color: rgba(255, 255, 255, 0.95);
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 50rem;
  width: 80%;
  margin: auto;
}
</style>
