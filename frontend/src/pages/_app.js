// pages/_app.js
import { store } from "../../store/index";
import "@/styles/globals.css";
import { Provider } from 'react-redux';
export default function App({ Component, pageProps }) {
  return (
    <>
    <Provider store={store}>
        
      <div className="bg-gray-800">
      <Component {...pageProps} />
      </div>
    </Provider>

    </>
  );
}