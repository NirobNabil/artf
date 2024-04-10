import React, { useState } from "react";
// import axios from "axios";
import Image from "next/image";

const FileUploadForm = () => {
  const [loadedImages, setLoadedImages] = useState([]);
  const [selectedImages, setSelectedImages] = useState([]);

  const handleFileChange = (event) => {
      setSelectedImages(event.target.files)
      // const fileMetaDatas = event.target.files;
      // for (let i = 0; i < fileMetaDatas.length; i++) {
      //   const fr = new FileReader();
      //   fr.onload = () => {
      //     setLoadedImages((prev) => [...prev, fr.result]);
      //   };
      //   fr.readAsDataURL(fileMetaDatas[i]);
      // }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    const form = event.currentTarget;
    const url = new URL("http://127.0.0.1:8080/fileupload");
    const formData = new FormData();

    console.log(selectedImages)

    Array.from(selectedImages).forEach( (image, i) => {
      formData.append( `sample-${i+1}.jpg`, image )
    } )

    const fetchOptions = {
      method: 'post',
      body: formData
    };

    fetch(url, fetchOptions);

  };

  return (
    <div className="container">
      <div className="form-wrapper">
        <form onSubmit={handleSubmit}>
          <div className="flex">
            {loadedImages.map((image, index) => (
              <div key={index} className="mb-4">
                <Image
                  src={image}
                  alt="Uploaded Image"
                  height={500}
                  width={500}
                />
              </div>
            ))}
          </div>
          <input
            type="file"
            multiple
            onChange={handleFileChange}
            className="border border-gray-300 rounded p-2 w-full mb-4"
          />
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
          >
            Upload
          </button>
        </form>
      </div>
    </div>
  );
};

export default FileUploadForm;
