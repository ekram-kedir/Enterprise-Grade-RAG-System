// store/index.js
import { configureStore } from "@reduxjs/toolkit";
import { chat } from "./feature/chat";  // Adjust the path accordingly

export const store = configureStore({
  reducer: {
    [chat.reducerPath]: chat.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(chat.middleware),
});

export const RootState = store.getState;
export const AppDispatch = store.dispatch;
