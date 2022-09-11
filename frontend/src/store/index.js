import createPersistedState from "vuex-persistedstate";
import { Store } from 'vuex';
import { createStore } from "vuex-extensions";

import notes from './modules/notes';
import users from './modules/users';


export default createStore(Store, {
  modules: {
    notes,
    users,
  },
  plugins: [
    createPersistedState()
  ]
});
