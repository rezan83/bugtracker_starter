# The challenge

This Readme will guide you through it. It will first present a high level full picture of the project and then scope your task.

In order to run the code for the frontend and the api, please check out the `api/README.md` and the `frontend/README.md`.

## Technologies

Backend: Python and fastapi
Frontend: Vuejs, Nuxt, Tailwind css

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

## The task

errors sorted into the 3 available categories: resolved, unresolved, backlog.

The tasks are split across the frontend and the api, the main focus lies on data manipulation and UI/UX implementation.

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
