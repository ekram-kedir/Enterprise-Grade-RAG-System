// store/features/chat/index.js
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

const API_BASE_URL = "http://127.0.0.1:5000";

export const chat = createApi({
  reducerPath: "chat",
  baseQuery: fetchBaseQuery({ baseUrl: API_BASE_URL }),
  endpoints: (builder) => ({
    postMessage: builder.query({
      query: (message) => ({
        url: "/api/chat",
        method: "POST",
        body: { string: message },
      }),
    }),
  }),
});

export const { usePostMessageQuery } = chat;

// Exporting a custom function for mutation if needed
export const usePostMessageMutation = () => {
  // The mutate function can be implemented based on your needs
  const mutate = async (message) => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ string: message }),
      });

      if (!response.ok) {
        throw new Error("Failed to post message");
      }

      const data = await response.json();
      return data;
    } catch (error) {
      throw new Error("Failed to post message");
    }
  };

  // Return an object with the mutate function
  return { mutate };
};
