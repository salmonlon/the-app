<template>
    <div>

        <section class="row mt-4">
            <h1>Users</h1>
            <hr />

            <div v-if="users.length">
                <div class="row row-cols-3">
                    <div v-for="user in users" :key="user.id" class="users">
                        <div class="card col">
                            <div class="card-body">
                                <ul>
                                    <li><strong>Username:</strong> {{ user.username }}</li>
                                    <li><strong>Email:</strong> {{ user.email }}</li>
                                    <li>
                                        <router-link :to="{ name: 'User', params: { id: user.id } }">View</router-link>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <br />
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
    name: 'Admin',
    data() {
        return {
        };
    },
    created: function () {
        return this.$store.dispatch('getActiveNotes');
    },
    computed: {
        // https://v3.vuex.vuejs.org/guide/getters.html#the-mapgetters-helper
        ...mapGetters(
            { users: 'stateUsers' }
        ),
    },
    methods: {

    },
};
</script>