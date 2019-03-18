import React, {
    Component,
    Fragment
} from "react";
import ReactDOM from "react-dom";
import {
    HashRouter as Router,
    Route,
    Switch,
    Redirect
} from "react-router-dom";

import {
    Provider as AlertProvider
} from "react-alert";
import AlertTemplate from "react-alert-template-basic";


class App extends Component {
    render() {
        return <h1 > fdasdf < /h1>
    }
}

ReactDOM.render( < App / > , document.getElementById("app"));