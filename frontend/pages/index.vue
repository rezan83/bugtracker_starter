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
      </div>
    </nav>
    <div
      v-if="reseted"
      class="flex fixed top-0 w-full justify-between items-center flex-wrap h-12 shadow-xl px-2 my-2 mx-2 bg-green-300"
    >reseted successfully</div>
    <div class="mt-200">
      <div>
        <div class="min-w-25 text-lg bg-blue-200 py-2 px-4 mx-2 mt-8 h-16">Unsolved</div>
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
        <div class="min-w-25 text-lg bg-blue-200 py-2 px-4 mx-2 mt-8 h-16">Resolved</div>
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
        <div class="min-w-25 text-lg bg-blue-200 py-2 px-4 mx-2 mt-8 h-16">Backlog</div>
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
    replace: function(item, array1, array2) {
      this.lastItem = item;
      this.lastIndex = array1.indexOf(item);
      this.fromArry = array2;
      this.toArry = array1;
      array1.splice(array1.indexOf(item), 1);
      array2.push(item);
    },
    unresolve: function(issue) {
      this.replace(issue, this.resolved, this.unresolved);
    },
    resolve: function(issue) {
      this.replace(issue, this.unresolved, this.resolved);
    },
    moveUp: function(issue) {
      this.replace(issue, this.backlog, this.unresolved);
    },
    undo: function() {
      if (this.lastItem) {
        this.fromArry.splice(this.fromArry.indexOf(this.lastItem), 1);
        this.toArry.splice(this.lastIndex, 0, this.lastItem);
        this.lastItem = this.fromArry = this.toArry = this.lastIndex = null;
      }
    },
    reset: function() {
      this.resolved = this.store.resolved;
      this.unresolved = this.store.unresolved;
      this.backlog = this.store.backlog;
      this.reseted = true;
      setTimeout(() => {
        this.reseted = false;
      }, 1000);
    }
  },
  data() {
    return {
      resolved: [],
      unresolved: [],
      backlog: [],
      store: {},
      lastItem: null,
      lastIndex: null,
      fromArry: null,
      toArry: null,
      reseted: false
    };
  }
};
</script>
