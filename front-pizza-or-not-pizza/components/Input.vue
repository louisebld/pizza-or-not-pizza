<script>
import axios from "axios";

export default {
  data() {
    return {
      answer: "",
    };
  },
  methods: {
    sendFile() {
      console.log("File sent");
      const file = document.querySelector("input[type=file]").files[0];
      const formData = new FormData();
      formData.append("file", file);

      axios.post("http://localhost:8000/predict", formData).then((response) => {
        console.log(response.data);
        this.answer = response.data;
      });
    },
  },
};
</script>
<template>
  <div>
    <input type="file" />
    <button @click="sendFile">Send</button>
    <p>{{ answer }}</p>
  </div>
</template>

