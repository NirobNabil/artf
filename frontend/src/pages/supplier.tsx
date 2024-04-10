import FileUploaderForm from "../../components/FileUploadForm";

export default function Page() {
  return (
    <div className="bg-gray-900 min-h-screen flex flex-col justify-center items-center p-6">
      <div className="w-full p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <h1 className="text-6xl font-bold text-gray-900 opacity-70 my-10">
            Product Details
        </h1>
        <FileUploaderForm />
      </div>
    </div>
  );
}
