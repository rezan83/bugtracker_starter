# Coding challenge

Welcome to this fullstack coding challenge. This Readme will guide you through it. It will first present a high level full picture of the project and then scope your task.

In order to run the code that already exists for the frontend and the api, please check out the `api/README.md` and the `frontend/README.md`.

## High Level Description

Our company wants to write a checking tool for internal JSONs that store data. These JSONs are checked, everytime our checking system finds an error, it generates a JSON error object like:

```json
{
  "index": SOME_NUMERIC_INDEX,
  "code": SOME_NUMERIC_ERROR_CODE,
  "text": SOME_TEXT_DESCRIPTION
}
```

We then wrote an API that will get all errors generated so far, seperated by their status. A human operator has to be able to see and understand these errors in order to fix them in the original data. Our company strives to reduce errors to almost zero by providing a flawless UI/UX for operators to check errors and resolve them.

## Your task

Some other developer already wrote an API that delivers errors sorted into the 3 available categories: resolved, unresolved, backlog. Another developer has already started on the frontend, but he only did the bare minimum.

Your tasks are split across the frontend and the api, the main focus lies on data manipulation and UI/UX implementation.

Please check all tasks that you completed. Please document everything that should be documented. For example, if you chose to implement a stretch goal functionality that is not part of the list.

This challenge should work for all styles of developers:

- Fullstack developers may choose to work on _frontend_ and _backend_ tasks,
- Frontend developers may choose to focus on _frontend_ tasks and work on additional _backend_ tasks if they so choose,
- Backend developers may choose to focus on _backend_ tasks and work on additional _frontend_ tasks if they so choose.

Feel compelled to focus your work on the tasks that you would like to perform or the tasks that you have a good idea for. If you are stuck on something, don't give up! Just commit whatever you came up with and move on to another part of the challenge.

You may submit notes, feedback or any additional information that you _want_ to give and that cannnot be part of the codebase if you'd like. This is optional.

_frontend_

- [x] Write a UI that allows the operator to:
  - [x] have an "nice" overview of all errors, it should show `unresolved`, then `resolved` and then `backlog` errors
  - [x] see the `text` and `code` of each error
  - [x] resolve each individual `unresolved` error by clicking an individual button
  - [x] unresolve each individual `resolved` error (e.g., when an error was set to `resolved` by mistake) by clicking an individual button
  - [x] move an individual backlog error to the bottom of the `unresolved` list of displayed errors, by clicking an individual button
  - [x] undo his last action. E.g., if he resolved an unresolved error, an `undo` functionality enables him to move it back into the unresolved list of errors. This should work between all lists for _ only the last_ action of a user

_backend_

- [x] write a logging functionality, that counts how many requests for errors are received (you can store these numbers in memory, no persistent storage required)
- [x] implement the code of the `get_list_intersection_counts` function endpoint. You can find it in `_api.py`, it contains an extensive documentation string, that should define the problem well.

This is the absolute minimum our operators and their managers need, in order to resolve errors effectively. If you still have time/if you're still willing, you may start on the `version two` - this will enable our operators to resolve errors _effectively_ (frontend version two) and us to check the system for systematic errors (api version two).

_frontend version two_

- [x] make the UI/UX better
  - [x] shadows,
  - [x] click, hover animations (e.g. changing to a darker shade of said color)
  - [x] notifications
  - [x] mobile layout
  - [x] ...
- [x] make the undo functionality better
  - [x] the user should be able to undo _all_ of his actions
  - [x] when a user clicks undo, the item that switches lists should be in the same position as before (e.g., if the user resolved an error that was in the middle of the list at position 4, it should also re-appear at position 4 if he undoes this action)

_api version two_

- [x] add the `operator_name` as a parameter to the request that is sent from the `frontend` to the `api` to get the error lists. Then log how many times a certain operator requested data (you can store these numbers in memory, no persistent storage required). You may hardcode a name in the frontend, e.g., `operator_name: 'YOUR NAME'`.
- [x] add a new functionality: The operator can send all errors that are currently marked as `resolved` to the `api`, the `api` prints out how many times a certain `error.code` was resolved

Note: These are in no particular order, start and do whatever you like. If you have a good idea on how to solve one of these problems, it would be a good idea to start with that problem. We appreaciate nice UI/UX implementations, but we also appreaciate efficient and smart data structure/logic implementations.

If you have an additional idea, that would bring our operators forward and is not on this stretch goal list, please feel free to implement that as well, or even just write about it in this or some other file. We also love people that think about their tasks and are able to think like the people whose problems they solve.

## Screenshots

Some screenshots to get you started/so that you know, that you're on the right path.

[frontend output](./screenshots/start_frontend_output.png) shows the raw, initial frontend that the previous developer left for you.

[terminal output](./screenshots/start_terminal_output.png) show the raw terminal output, that you will see once you ran all the correct commands to get the frontend and api started.
