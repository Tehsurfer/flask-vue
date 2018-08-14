<template>
  <div id="app">
    <h1>Web App</h1>
    <h4>Dataset: {{ datasetName }}</h4>
    <input autofocus type="text" placeholder="Enter a Dataset ID" v-model="datasetId">
    <button :disabled="isLoading" @click="getDataset">Submit</button>
  </div>
</template>

<script>
export default {
  name: 'app',

  data() {
    return {
      datasetName: '',
      datasetId: '',
      isLoading: false
    }
  },

  methods: {
    getDataset() {
      if (!this.datasetId) {
        return
      }

      this.isLoading = true

      const url = `http://127.0.0.1:8000/api/dataset/${this.datasetId}`

      fetch(url)
        .then(response => response.text())
        .then(data => {
          this.datasetName = data
          this.isLoading = false
        })
        .catch(err => {
          this.isLoading = false
          console.error(err)
        })
    }
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

input {
  outline: none;
  padding: 10px;
  margin-right: 8px;
}

button {

}
</style>
