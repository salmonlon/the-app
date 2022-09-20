<template>
  <div>
    <section class="row">
      <h1>Focus</h1>
      <hr/>

      <form ref="taskForm" @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Task:</label>
          <input 
            type="text" 
            name="title" 
            v-model="form.title" 
            class="form-control" />
            <div v-if="v$.form.title.$error">Task needs to have a title</div>
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Note:</label>
          <textarea
            name="content"
            v-model="form.content"
            class="form-control"
          ></textarea>
        </div>
        <!-- TODO: use  Vue Gesture for due date selection -->
        <button type="submit" class="btn btn-primary">Do it now!</button>
      </form>
    </section>


    <section class="row mt-4">
      <h1>Notes</h1>
      <hr/>

      <div v-if="notes.length">
        <div class="row row-cols-3">
          <div v-for="note in notes" :key="note.id" v-bind:id="note.id" class="notes">
            <div class="card col">
              <div class="card-header">
                <router-link class="card-link" :to="{ name: 'Note', params: { id: note.id }}">{{ note.title }}</router-link>
              </div>
              <!-- <router-link class="card-link" :to="{ name: 'Note', params: { id: note.id }}"> {{ note.title }} </router-link> -->
              <!-- <li> {{ note.status }}</li> -->
              
              <!-- <li><strong>Author:</strong> {{ note.author.username }}</li> -->
              <!-- <li><router-link :to="{name: 'Note', params: { id: note.id }}">View</router-link></li> -->

              <div class="card-body">

                Due by {{ format(parseISO(note.due_date), 'dd/MM/yyyy kk:mm') }} 

              </div>


              <div class="card-footer"> 


                <div class="row row-cols-2 justify-content-around">
                  <button v-on:click="complete(note.id)" type="button" class="btn btn-success col-5">Done</button>
                  <button type="button" class="btn btn-warning col-5">Later</button>
                </div>

              </div>
            <!-- <br/> -->
            </div>
          </div>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import useVuelidate from '@vuelidate/core'
import { required } from '@vuelidate/validators'
import { format, parseISO } from 'date-fns'
// import { utcToZonedTime } from 'date-fns-tz'

export default {
  name: 'Dashboard',
  setup () {
    return { 
      v$: useVuelidate(),
      format,
      parseISO,
      // utcToZonedTime,
    }
  },
  data() {
    return {
      form: {
        title: '',
        content: ''
      },
    };
  },
  validations() {
    return {
      form: {
        title: { required, $lazy: true },
        // content: { },
        // due_date: { },
      }
    }
  },
  created: function() {
    return this.$store.dispatch('getActiveNotes');
  },
  computed: {
    // https://v3.vuex.vuejs.org/guide/getters.html#the-mapgetters-helper
    ...mapGetters(
        { notes: 'stateNotes'}
      )
  },
  methods: {
    ...mapActions(['createNote']),
    async submit() {
      const isFormCorrect = await this.v$.$validate()

      if (isFormCorrect) {
        let due_date = new Date()
        due_date.setHours(17)
        due_date.setMinutes(0)
        due_date.setSeconds(0)
        this.form.due_date = due_date.toISOString()
        // console.log(this.form);
        await this.createNote(this.form);
        this.$refs.taskForm.reset();
      } else {
        // TODO: show error message
      }

    },

    ...mapActions(['completeNote']),
    async complete(id) {
      await this.completeNote(id);
    },

  },
};
</script>