import React, { Component } from 'react';
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from './CreateRoomPage';
import Room from "./Room";
import {
    BrowserRouter as Router,
    Routes,
    Route,
    Link,
    Redirect,
  } from "react-router-dom";


export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
        <Router>
            <Routes>
                <Route exact path="/" element={
                    <p>This is the home page.</p>
                }></Route>
                <Route path="/join" >
                    <RoomJoinPage />
                </Route>
                <Route path="/create" >
                    <CreateRoomPage />
                    </Route>
                <Route path="/room/:roomCode" >
                    <Room />
                </Route>
            </Routes>
        </Router>
        );
    }
}
