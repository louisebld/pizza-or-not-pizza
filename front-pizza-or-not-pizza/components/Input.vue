<script>
import axios from "axios";
import { Pie } from "vue-chartjs";

import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
ChartJS.register(ArcElement, Tooltip, Legend);

export default {
  components: { Pie },
  data() {
    return {
      value: "",
      file: "",
      chart: null,
      loaded: false,
      error: "",
      chartData: {
        labels: ["Which pizza are you?"],
        datasets: [
          {
            label: "Pizza",
            data: [1],
            backgroundColor: ["rgba(255, 99, 132, 0.2)"],
            borderColor: ["rgba(255, 99, 132, 1)"],
            borderWidth: 1,
          },
        ],
      },
    };
  },

  methods: {
    sendFile() {
      console.log("File sent");
      const file = document.querySelector("input[type=file]").files[0];
      const formData = new FormData();
      formData.append("file", file);

      axios.post("http://localhost:8000/predict", formData).then((response) => {
        this.value = response.data;
        this.chartData = response.data;
        this.isloaded = true;

        console.log(response.data);

        if (response.data.error) {
          this.error = response.data.error;
        }

        const labels = response.data.map((pizza) => pizza.label);
        const data = response.data.map((pizza) => pizza.score);

        this.chartData = {
          labels: labels,
          datasets: [
            {
              label: "Pizza",
              data: data,
              backgroundColor: [
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
              ],
              borderColor: [
                "rgba(255, 99, 132, 1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
              ],
              borderWidth: 1,
            },
          ],
        };
      });
    },
  },
};
</script>

<template>
  <div>
    <input type="file" @change="file = $event.target.files[0]" />
    <button @click="sendFile">Envoyer</button>
  </div>
  <div v-if="value" class="result">
    <div class="pie">
      <Pie :data="chartData" :options="chartOptions" />
    </div>
    Vous êtes une {{ value[0].label }} avec une probabilité de
    {{ Math.round(value[0].score * 100) }}%
  </div>
  <div v-if="error" class="error">{{ error }}</div>
</template>

<style>
.pie {
  width: 30rem;
  height: 30rem;
}

.result {
  display: flex;
  flex-direction: column;
  align-items: center;
}

button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  border: none;
  background-color: #f1f1f1;
  cursor: pointer;
  transition: 0.3s;
}
</style>
