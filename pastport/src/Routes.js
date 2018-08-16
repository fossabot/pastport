import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./containers/Home";
import NotFound from "./containers/NotFound";
import Login from "./containers/Login";
import Admin from "./containers/Admin";

export default () =>
    <Switch>
        <Route path="/login" exact component={Login} />
        <Route path="/admin" exact component={Admin} />
        <Route path="/" exact component={Home} />
        <Route component={NotFound} />
    </Switch>;