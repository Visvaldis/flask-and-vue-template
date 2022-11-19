<template>
 <v-container
 fluid
 style="height: 100%;"
    >
      <v-row
      style="height: 100%;"
      >
        <v-col class="bg-secondary"  cols="3">
          <div color="secondary">
            Aside
          </div>
          
        </v-col>
        <v-col cols="9">
         <v-col cols="12" class="mb-3">
          <v-btn color="success" class="mr-3" @click="get()">Send GET </v-btn>
          <v-btn color="warning" class="ml-3" @click="post()">Send POST</v-btn>
        </v-col>
        <v-col cols="12">
          <v-card variant="tonal" :loading="loading" v-if="ifResult" width="400">
            <template v-slot:title>
              This is a {{title}} result
            </template>

            <template v-slot:text v-if="result">
              {{result}}
            </template>
          </v-card>
        </v-col>
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: "MainPage",

  data: () => ({
      smart: false,
    loading: false,
    ifResult: false,
    result: {},
    title: ""
  }),
  methods: {
    photoUploaded(file) {
      console.log(file);
      this.predictedCategory = '';
      if (file) {
        this.photoUrl = URL.createObjectURL(file);
      }
    },

      get(){
      let path = `http://localhost:5000/get/4`;
     
      this.loading = true; 
      axios.get(path)
        .then((response) => {
          this.loading = false; 
          this.ifResult = true;
          this.title = "GET"
          this.result = JSON.stringify(response.data);
          console.log(this.result);
        }).catch((error) => {
           this.ifResult = false;
           console.log(error);
        });

     
    },
    post(){
      let path = `http://localhost:5000/post`;

      this.loading = true; 
      let data = {
        title: "test",
        text: "test test"
      }
      axios.post(path, data)
        .then((response) => {
          this.loading = false; 
          this.ifResult = true;
          this.title = "POST"
          this.result = JSON.stringify(response.data);
          console.log(this.result);
        }).catch((error) => {
           this.ifResult = false;
           console.log(error);
        });

     
    }

  },
  computed: {},
};
</script>
<style scoped>

</style>
