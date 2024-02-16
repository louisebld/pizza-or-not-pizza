<script>
import axios from "axios";

export default {
  data() {
    return {
      value: "",
      pourcentage: "",
    };
  },
  methods: {
    sendFile() {
      console.log("File sent");
      const file = document.querySelector("input[type=file]").files[0];
      const formData = new FormData();
      formData.append("file", file);

      axios.post("http://localhost:8000/predict", formData).then((response) => {
        this.extractAnswer(response);
      });
    },
    extractAnswer(response) {
      this.value = response.data[0].label;
      this.pourcentage = response.data[0].score;
      this.pourcentage = Math.round(this.pourcentage * 100);
    },
  },
};
</script>

<template>
  <div>
    <input type="file" />
    <button @click="sendFile">Send</button>
    <div v-if="value != ''">
      <p v-if="value == 'pizza'">{{ pourcentage }}% of PIZZA</p>
      <p v-else>{{ pourcentage }}% of NOT PIZZA</p>
    </div>
  </div>
</template>

