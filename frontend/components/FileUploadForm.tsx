import React, { useState } from "react";
// import axios from "axios";
import Image from "next/image";

const FileUploadForm = () => {
  const [loadedImages, setLoadedImages] = useState([]);
  const [selectedImages, setSelectedImages] = useState([]);

  const handleFileChange = (event) => {
      setSelectedImages(event.target.files)
      const fileMetaDatas = event.target.files;
      for (let i = 0; i < fileMetaDatas.length; i++) {
        const fr = new FileReader();
        fr.onload = () => {
          setLoadedImages((prev) => [...prev, fr.result]);
        };
        fr.readAsDataURL(fileMetaDatas[i]);
      }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    const form = event.currentTarget;
    const url = new URL("http://127.0.0.1:8080/fileupload");
    const formData = new FormData(event.target);

    Array.from(selectedImages).forEach( (image, i) => {
      formData.append( `image-${i+1}.jpg`, image )
    } )

    console.log(formData)

    const fetchOptions = {
      method: 'post',
      body: formData
    };

    // fetch(url, fetchOptions);

  };

  return (
    <form className="flex flex-col gap-y-4"  onSubmit={handleSubmit}>
      
      <input type="text" name="productName" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Nezuko Keychain" required />
      <input type="text" name="height" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="45cm" required />
      <input type="text" name="width" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="20cm" required />
      
      <div className="flex">
        {loadedImages.map((image, index) => {
          if (index > 4){
            return <></>
          }
          return (
          <div key={index} className="mb-4">
            <Image
              src={image}
              alt="Uploaded Image"
              height={500}
              width={500}
            />
          </div>
        )})}
      </div>
      <input
        type="file"
        multiple
        onChange={handleFileChange}
        className="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
      />
      <button
        type="submit"
        className="my-8 text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
      >
        Upload
      </button>
    </form>
  );
};

export default FileUploadForm;
