import { BrowserRouter, Routes, Route, } from "react-router-dom";

import React, { Component } from 'react';
import MainPage from "./pages/MainPage/MainPage";
import PollsPage from "./pages/PollsPage/PollsPage";
import ProfilePage from "./pages/ProfilePage/ProfilePage";
import EnterPage from "./pages/Auth/AuthorizPage";
import CreatePage from "./pages/CreatePage/CreatePage";
import ConstructorPage from "./pages/ConstructorPage/ConstructorPage";
import Passing from "./pages/PollsPassing/Passing";
import LogoutWithotPage from "./pages/Auth/LogoutWithotPage";


class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<MainPage />} />

          <Route path="/profile/" element={<ProfilePage />} />
          <Route path="/auth/login/" element={<EnterPage />} />
          <Route path="/auth/logout/" element={<LogoutWithotPage/>}/>


          <Route path="/polls/" element={<PollsPage />} />

          <Route path="/polls/create/" element={<CreatePage />} />
          <Route path="/polls/constructor/" element={<ConstructorPage />} />

          <Route path="/polls/:slug/" element={<Passing />} />
        </Routes>
      </BrowserRouter>
    );

  }
}
export default App;