<template>
    <section>
        <h1>Users</h1>
        <hr/><br/>

        <div v-if="users.length">
            <div v-for="user in users" :key="user.id" class="users">
                <div class="card" style="width: 18rem;">
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
    </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    name: 'Admin', 
    created: function() {
        return this.$store.dispatch('allUsers');
    },
    computed: {
        ...mapGetters({users: 'stateUsers' }),
    },
    methods: {

    },
}
</script>