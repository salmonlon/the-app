import axios from 'axios';
import store from '@/store';

const state = {
  notes: null,
  note: null
};

// retrieves the values of state.note and state.notes
const getters = {
  stateNotes: state => state.notes,
  stateNote: state => state.note,
};

// actions make HTTP calls via Axios and a few of them perform a side effect by calling relevant mutations
const actions = {

  // {} is used for argument distructuring the context object (commit, dispatch, getters, state...)
  async createNote({dispatch}, note) {
    await axios.post('notes', note);
    await dispatch('getActiveNotes');
  },
  async getNotes({commit}) {
    let {data} = await axios.get('notes');
    commit('setNotes', data);
  },
  async getActiveNotes({commit}) {
    // use rootState for accessing username
    let {data} = await axios.get('notes', {
      params: {
        status: 'active', 
        user: store.getters.stateUser.username
      }
    });
    commit('setNotes', data);
  },
  async viewNote({commit}, id) {
    let {data} = await axios.get(`notes/${id}`);
    commit('setNote', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateNote({}, note) {
    await axios.patch(`notes/${note.id}`, note.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteNote({}, id) {
    await axios.delete(`notes/${id}`);
    // TODO: clear note state
  },
  async completeNote({dispatch}, id) {
    await axios.patch(`notes/${id}/complete`);
    // TODO: refresh the current note only
    await dispatch('getActiveNotes');
  }
};

// make changes to state
const mutations = {

  // mutation receive the state and additional arguments, wrapped in an object
  setNotes(state, notes){
    state.notes = notes;
  },
  setNote(state, note){
    state.note = note;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};