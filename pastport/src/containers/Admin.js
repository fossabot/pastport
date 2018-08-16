import React, { Component } from 'react';
import axios from 'axios';

class Admin extends Component {
    constructor(props) {
        super(props)
        this.state = {
            lists: []
        }
    }
    componentDidMount() {
        axios.get('/users')
            .then(response => {
                console.log(response)
                this.setState({
                    lists: response.data.Users
                })
            })
            .catch(error => console.log(error))
    }
    render() {
        return (
            <div className="lists-container">
                {this.state.lists.map((list, index) => {
                    return (
                        <div className="single-list" key={index}>
                            <h4>{list.email}</h4>
                            <p>{list.name}</p>
                        </div>
                    )
                })}
            </div>
        )
    }
}
export default Admin;