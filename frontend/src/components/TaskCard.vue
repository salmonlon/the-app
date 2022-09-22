<template>
    <div class="card mb-3" style="max-width: 18rem;">
        <div class="card-header">
            <!-- <router-link class="card-link text-white" :to="{ name: 'Note', params: { id: note.id }}">{{ note.title }}</router-link> -->
            <h5 class="card-title">{{ note.title }}</h5>
        </div>
        <!-- <router-link class="card-link" :to="{ name: 'Note', params: { id: note.id }}"> {{ note.title }} </router-link> -->
        <!-- <li> {{ note.status }}</li> -->

        <!-- <li><strong>Author:</strong> {{ note.author.username }}</li> -->
        <!-- <li><router-link :to="{name: 'Note', params: { id: note.id }}">View</router-link></li> -->

        <div class="card-body" :class="{'text-danger': isDateOverdue(note.due_date)}">

            Due by {{ formatLocal(note.due_date) }}

        </div>


        <div class="card-footer">


            <div class="row row-cols-2 justify-content-around">
                <button v-on:click="complete(note.id)" type="button" class="btn btn-success col-5">Done</button>

                <div class="btn-group">
                    <button type="button" class="btn btn-warning"
                        v-on:click="delayNote(note, 'tomorrow')">Tomorrow</button>
                    <button type="button" class="btn btn-warning dropdown-toggle dropdown-toggle-split"
                        data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        <span class="sr-only"></span>
                    </button>
                    <div class="dropdown-menu">
                        <a class="dropdown-item" v-on:click="delayNote(note, 'later')" href="#">Later this week</a>
                        <a class="dropdown-item" v-on:click="delayNote(note, 'weekend')" href="#">This weekend</a>
                        <!-- <a class="dropdown-item" href="#">I give up</a> -->
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" v-on:click="delete_note(note.id)" href="#">Delete</a>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import { format, parseISO, compareAsc } from 'date-fns'
import { mapActions } from 'vuex';

export default {
    props: ['note'],

    methods: {
        isDateOverdue(date) {
            return compareAsc(parseISO(date), new Date()) < 0;
        },
        formatLocal(date) {
            return format(parseISO(date), "dd/MM/yyyy kk:mm");
        },
        ...mapActions(["completeNote"]),
        async complete(id) {
            await this.completeNote(id);
        },
        ...mapActions(["updateNote"]),
        async delayNote(note, delayBy) {
            let due_date = parseISO(note.due_date);
            // if (due_date < new Date()) {
            //   due_date = new Date()
            // }
            due_date = new Date();
            if (delayBy == "tomorrow") {
                due_date.setDate(new Date().getDate() + 1);
            }
            else if (delayBy == "later") {
                due_date.setDate(new Date().getDate() + 3);
            }
            else if (delayBy == "weekend") {
                if (due_date.getDay() < 6) {
                    due_date.setDate(new Date().getDate() + (6 - due_date.getDay()));
                }
            }
            note.due_date = due_date.toISOString();
            let update_note = {
                id: note.id,
                form: {
                    due_date: note.due_date
                }
            };
            await this.updateNote(update_note);
            // this.$refs.taskForm.reset();
        },
        ...mapActions(["deleteNote"]),
        async delete_note(id) {
            await this.deleteNote(id);
        },
    }

}
</script>

<style lang="scss" scoped>

</style>