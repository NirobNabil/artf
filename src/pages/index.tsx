import FileUploaderForm from "../../components/FileUploadForm";

export default function Page() {
  return (
    <div className="bg-gray-900 min-h-screen flex flex-col justify-center items-center">
      <h1 className="text-6xl font-bold text-white mb-8 opacity-70">
        Art-<span className="text-blue-500"></span>F
      </h1>
      <div className="bg-gray-700 rounded-lg shadow-xl w-full max-w-xl p-8">
        <h2 className="text-4xl font-bold mb-6 text-white text-center opacity-70">
          Upload Files
        </h2>
        <div className="max-w-lg mx-auto h-full">
          <FileUploaderForm />
        </div>
        <div className="flex justify-center mt-8">
          <a
            href="#"
            className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded inline-block"
          >
            Upload
          </a>
        </div>
      </div>
    </div>
  );
}
