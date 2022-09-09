<template>
  <div>
    <section class="row">
      <h1>How's your day?</h1>
      <hr/>

      <form ref="taskForm" @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Task:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Note:</label>
          <textarea
            name="content"
            v-model="form.content"
            class="form-control"
          ></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>


    <section class="row mt-4">
      <h1>Notes</h1>
      <hr/>

      <div v-if="notes.length">
        <div class="row row-cols-3">
          <div v-for="note in notes" :key="note.id" v-bind:id="note.id" class="notes">
            <div class="card col">
              <div class="card-body">
                <ul>
                  <li><strong>Note Title:</strong> {{ note.title }}</li>
                  <li> {{ note.status }}</li>
                  <!-- <li><strong>Author:</strong> {{ note.author.username }}</li> -->
                  <li><router-link :to="{name: 'Note', params:{id: note.id}}">View</router-link></li>
                </ul>

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
export default {
  name: 'Dashboard',
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
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
      // TODO: prevent submitting empty form
      await this.createNote(this.form);
      this.form = {
        title: '',
        content: '',
      };
    },

    ...mapActions(['completeNote']),
    async complete(id) {
      await this.completeNote(id);
    },

  },
};
</script>