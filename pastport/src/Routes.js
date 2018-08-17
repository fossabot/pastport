import React from "react";
import { Route, Switch } from "react-router-dom";
import Home from "./containers/Home";
import NotFound from "./containers/NotFound";
import Login from "./containers/Login";
import Admin from "./containers/Admin";
import Register from "./containers/Register";
import AppliedRoute from "./components/AppliedRoute";

export default ({ childProps }) =>
    <Switch>
        <Route path="/register" exact component={Register} />
        <AppliedRoute path="/login" exact component={Login} props={childProps} />
        <Route path="/admin" exact component={Admin} />
        <AppliedRoute path="/" exact component={Home} props={childProps} />
        <Route component={NotFound} />
    </Switch>;