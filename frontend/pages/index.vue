<template>
  <div class="text-gray-800 text-base">
    <nav class="flex fixed top-0 w-full items-center justify-between flex-wrap bg-blue-400 p-6">
      <div class="flex items-center flex-shrink-0 text-white mr-6">
        <span class="font-semibold text-xl tracking-tight">Bug Tracker</span>
      </div>
      <div>
        <button
          class="w-25 text-white bg-blue-500 hover:bg-blue-700 py-2 px-4"
          v-on:click="undo"
        >undo</button>
        <button
          class="w-25 text-white bg-red-500 hover:bg-red-700 py-2 px-4"
          v-on:click="reset"
        >reset</button>
        <button
          class="w-25 text-white bg-green-500 hover:bg-green-700 py-2 px-4"
          v-on:click="submitResulved"
        >submit</button>
      </div>
    </nav>
    <div
      class="flash-message flex fixed top-0 w-full justify-between items-center flex-wrap h-12 shadow-xl px-2 my-2 mx-2 bg-green-300"
      v-if="reseted"
    >{{ message }}</div>
    <div
      class="flash-message flex fixed top-0 w-full justify-between items-center flex-wrap h-12 shadow-xl px-2 my-2 mx-2 bg-green-300"
      v-if="undone"
    >{{ message }}</div>
    <div class="mt-200">
      <div>
        <div class="flex w-full justify-center items-center bg-blue-200 py-2 px-4 mx-2 mt-8 h-16">
          <h3>Unresolved</h3>
        </div>

        <div
          v-for="issue in unresolved"
          class="flex justify-between rounded-l-full items-center flex-wrap h-12 shadow-md px-2 my-2 mx-2 bg-red-300 hover:bg-red-400"
          :key="issue.id"
        >
          <div>
            <span>{{ issue.code }}</span>
            <span>{{ issue.text }}</span>
          </div>
          <button
            class="w-25 text-white bg-blue-500 hover:bg-blue-700 py-1 px-2"
            v-on:click="resolve(issue)"
          >resolve</button>
        </div>
      </div>
      <div>
        <div class="flex w-full justify-center items-center bg-blue-200 py-2 px-4 mx-2 mt-8 h-16">
          <h3>Resolved</h3>
        </div>
        <div
          class="flex justify-between rounded-l-full items-center flex-wrap h-12 shadow-md px-2 my-2 mx-2 bg-green-300 hover:bg-green-400"
          v-for="issue in resolved"
          :key="issue.id"
        >
          <div>
            <span>{{ issue.code }}</span>
            <span>{{ issue.text }}</span>
          </div>
          <button
            class="w-25 text-white bg-red-500 hover:bg-red-700 py-2 px-4"
            v-on:click="unresolve(issue)"
          >unresolve</button>
        </div>
      </div>
      <div>
        <div class="flex w-full justify-center items-center bg-blue-200 py-2 px-4 mx-2 mt-8 h-16">
          <h3>Backlog</h3>
        </div>
        <div
          class="flex justify-between rounded-l-full items-center flex-wrap h-12 shadow-md px-2 my-2 mx-2 bg-purple-300 hover:bg-purple-400"
          v-for="issue in backlog"
          :key="issue.id"
        >
          <div>
            <span>{{ issue.code }}</span>
            <span>{{ issue.text }}</span>
          </div>
          <button
            class="w-25 text-white bg-red-500 hover:bg-red-700 py-2 px-4"
            v-on:click="moveUp(issue)"
          >move up</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// storing issues/errors for reseting when needed
var gStore = {};

export default {
  async asyncData({ $axios }) {
    try {
      const { resolved, unresolved, backlog } = await $axios.$get(
        "http://localhost:8000/get_lists"
      );

      gStore = {
        resolved: [...resolved],
        unresolved: [...unresolved],
        backlog: [...backlog]
      };
      const store = gStore;
      return {
        resolved,
        unresolved,
        backlog,
        store
      };
    } catch (error) {
      console.log(
        `Couldn't get error lists:\n${error}\nDid you start the API?`
      );
    }
  },
  methods: {
    // exchange item from first list to another and saving data for undo
    replace: function(item, array1, array2) {
      this.changedItem = item;
      this.changedIndex = array1.indexOf(item);
      this.fromArry = array2;
      this.toArry = array1;
      array1.splice(array1.indexOf(item), 1);
      array2.push(item);
    },
    resetMessage: function() {
      this.message = `reseted successfully`;
      this.reseted = true;
      setTimeout(() => {
        this.reseted = false;
      }, this.messageTime);
    },
    undoMessage: function(code) {
      this.message = `issue with code: ${code} undone successfully`;
      this.undone = true;
      setTimeout(() => {
        this.undone = false;
      }, this.messageTime);
    },
    unresolve: function(issue) {
      this.replace(issue, this.resolved, this.unresolved);
    },
    resolve: function(issue) {
      this.replace(issue, this.unresolved, this.resolved);
    },
    // move backlog item to unresolved
    moveUp: function(issue) {
      this.replace(issue, this.backlog, this.unresolved);
    },
    undo: function() {
      if (this.changedItem) {
        this.fromArry.splice(this.fromArry.indexOf(this.changedItem), 1);
        this.toArry.splice(this.changedIndex, 0, this.changedItem);
        this.undoMessage(this.changedItem.code);
        this.changedItem = this.fromArry = this.toArry = this.changedIndex = null;
      }
    },
    // undo-all/reset to original values
    reset: function() {
      this.resolved = this.store.resolved;
      this.unresolved = this.store.unresolved;
      this.backlog = this.store.backlog;
      this.resetMessage();
    },
    submitResulved: async function() {
      const data = {
        resolved: this.resolved
      };
      const res = await this.$axios({
        method: "put",
        url: "http://localhost:8000/put_resolved",
        data: data
      }).catch(e => console.log(e));
    }
  },
  data() {
    return {
      resolved: [],
      unresolved: [],
      backlog: [],
      store: {},
      changedItem: null,
      changedIndex: null,
      fromArry: null,
      toArry: null,
      reseted: false,
      undone: false,
      message: "",
      messageTime: 1500
    };
  }
};
</script>
