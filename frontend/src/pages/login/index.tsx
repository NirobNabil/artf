import React, { useState } from "react";
// import axios from "axios";
import Image from "next/image";
import FileUploadResultModal from "./FileUploadResultModal";

const FileUploadForm = () => {

    const [ loggedIn, setLoggedIn ] = useState(false)

    const handleSubmit = async (event) => {
        const url = new URL("http://127.0.0.1:8080/login");
        event.preventDefault();

        const form = event.currentTarget;
        const formData = new FormData(event.target);

        console.log(formData)

        const fetchOptions = {
            method: 'post',
            body: formData
        };

        fetch(url, fetchOptions).then(res => res.json()).then(res => {
            if( res.token ){
                localStorage.setItem('token', res.token)
                setLoggedIn(true)
            }
        })

    };

    return (
        <>
            <div className="bg-gray-900 min-h-screen flex flex-col justify-center items-center p-6">
                <div className="w-full p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                    <h1 className="text-6xl font-bold text-gray-900 opacity-70 my-10">
                        Sign in
                    </h1>
                    <form className="flex flex-col " style={{ rowGap: '15px' }} onSubmit={handleSubmit}>

                        <input type="text" name="username" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="username" required />
                        <input type="text" name="password" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="password" required />

                        <button
                            type="submit"
                            className="my-8 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
                        >
                            Login
                        </button>

                    </form>

                    { 
                        loggedIn && 
                        <div style={{ color: 'black' }} className="text-center border rounded-lg p-2 bg-slate-200" > Succesfully Logged in </div>
                    }
                </div>
            </div>

        </>
    );
};

export default FileUploadForm;
