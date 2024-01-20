// pages/index.js
import TypingAnimation from '../components/TypingAnimation';
import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { chatActions } from '../../store/feature/chat';

export default function Home() {
  const dispatch = useDispatch();
  const chatLog = useSelector((state) => state.chat.chatLog);
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    try {
      // Assuming there's some logic here to handle the user input
      // For now, let's add a user message to chatLog
      dispatch(chatActions.addMessage({ type: "user", message: inputValue }));

      // Assuming there's some logic here to generate a response
      // For now, let's add a bot message to chatLog
      dispatch(chatActions.addMessage({ type: "bot", message: "Bot response goes here" }));
    } catch (error) {
      console.error("Error posting message:", error);
      // Assuming setError is a valid action creator
      dispatch(chatActions.setError("Failed to post message"));
    }

    setInputValue('');
  };

  return (
    <div className="container mx-auto max-w-[700px] h-screen flex flex-col bg-black text-white">
      <h1 className="text-center py-3 font-bold text-4xl md:text-6xl">Your RAG</h1>
      <div className="flex-grow p-6 overflow-y-auto bg-black text-black rounded-lg mb-6">
        {chatLog && chatLog.map((message, index) => (
          <div key={index} className={`flex ${message.type === "user" ? "justify-end" : "justify-start"} mb-4`}>
            <div className={`p-4 rounded-lg max-w-[70%] ${message.type === "user" ? "bg-white text-black" : "bg-white text-black"} shadow-md`}>
              {message.message}
            </div>
          </div>
        ))}
        {/* Typing animation or any loading indicator */}
        {/* <div className="flex justify-start mb-4">
          <div className="p-4 rounded-lg max-w-[70%] bg-black text-black shadow-md">
            <TypingAnimation />
          </div>
        </div> */}
      </div>
      <form onSubmit={handleSubmit} className="p-6">
        <div className="flex rounded-lg border border-white">
          <input
            type="text"
            className="flex-grow px-4 py-2 bg-transparent text-white focus:outline-none"
            placeholder="Type your message..."
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
          />
          <button
            type="submit"
            className="bg-white rounded-lg px-4 py-2 text-black font-semibold focus:outline-none hover:bg-gray-200 transition-colors duration-300"
          >
            Send
          </button>
        </div>
      </form>
    </div>
  );
}
