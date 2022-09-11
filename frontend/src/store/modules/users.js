import axios from 'axios';

const state = {
  user: null,
  users: null
};

const getters = {
  isAuthenticated: state => !!state.user,
  isAdmin: state => state.user && state.user.role === 'admin',
  stateUser: state => state.user,
  stateUsers: state => state.users,
};

const actions = {
  async register({dispatch}, form) {
    await axios.post('register', form);
    let UserForm = new FormData();
    UserForm.append('username', form.username);
    UserForm.append('password', form.password);
    await dispatch('logIn', UserForm);
  },
  async logIn({dispatch}, user) {
    try {
      
      await axios.post('login', user);
      await dispatch('viewMe');
    } catch (error) {
      
      // show warning message
      console.log(error)
    }
  },
  async viewMe({commit}) {
    let {data} = await axios.get('users/whoami');
    await commit('setUser', data);
  },
  async getUsers({commit}) {
    let {data} = await axios.get('users');
    await commit('setUsers', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteUser({}, id) {
    await axios.delete(`user/${id}`);
  },
  async logOut({commit}) {
    commit('setUser', null);
    this.reset();
  }
};

const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  setUsers(state, users) {
    state.users = users;
  },
  logout(state, user){
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};