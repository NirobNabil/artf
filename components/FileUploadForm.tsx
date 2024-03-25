import React, { useState } from "react";
import axios from "axios";
import Image from "next/image";

const FileUploadForm = () => {
  const [loadedImages, setLoadedImages] = useState([]);

  const handleFileChange = (e) => {
    const fileMetaDatas = e.target.files;
    for (let i = 0; i < fileMetaDatas.length; i++) {
      const fr = new FileReader();
      fr.onload = () => {
        setLoadedImages((prev) => [...prev, fr.result]);
      };
      fr.readAsDataURL(fileMetaDatas[i]);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Add logic to handle form submission and image upload
    // const formData = new FormData();
    // formData.append('image', file);
    // try {
    //   const res = await axios.post('/api/upload', formData);
    //   console.log('Image uploaded:', res.data.imagePath);
    // } catch (error) {
    //   console.error('Error uploading image:', error.message);
    // }
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
          {/* <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
          >
            Upload
          </button> */}
        </form>
      </div>
    </div>
  );
};

export default FileUploadForm;
