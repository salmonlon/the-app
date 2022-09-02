<template>
  <div>
    <section class="row">
      <h1>Anything New?</h1>
      <hr/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
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
          <div v-for="note in notes" :key="note.id" class="notes">
            <div class="card col">
              <div class="card-body">
                <ul>
                  <li><strong>Note Title:</strong> {{ note.title }}</li>
                  <!-- <li><strong>Author:</strong> {{ note.author.username }}</li> -->
                  <li><router-link :to="{name: 'Note', params:{id: note.id}}">View</router-link></li>
                </ul>

                <div class="row row-cols-2 justify-content-around">
                  <button type="button" class="btn btn-success col-5">Done</button>
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

    <section class="row mt-4">
      <h1>Users</h1>
      <hr/>

      <div v-if="users.length">
        <div class="row row-cols-3">
          <div v-for="user in users" :key="user.id" class="users">
              <div class="card col">
                  <div class="card-body">
                      <ul>
                          <li><strong>Username:</strong> {{ user.username }}</li>
                          <li><strong>Email:</strong> {{ user.email }}</li>
                          <li><router-link :to="{name: 'User', params:{id: user.id}}">View</router-link></li>
                      </ul>
                  </div>
              </div>
              <br/>
          </div>
        </div>
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
    return this.$store.dispatch('getNotes');
  },
  computed: {
    // https://v3.vuex.vuejs.org/guide/getters.html#the-mapgetters-helper
    ...mapGetters(
        { notes: 'stateNotes'}
      ),
    ...mapGetters(
        { users: 'stateUsers' }
      ),
  },
  methods: {
    ...mapActions(['createNote']),
    async submit() {
      await this.createNote(this.form);
    },

    async completeNote() {
      await this.completeNote();
    },
  },
};
</script>