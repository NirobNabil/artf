import FileUploaderForm from "../../components/FileUploadForm";

export default function Page() {
  return (
    <div className="bg-gray-900 min-h-screen flex flex-col justify-center items-center p-8">
      <h1 className="text-6xl font-bold text-white mb-8 opacity-70">
        Product Details
      </h1>
      <div className="bg-gray-700 rounded-lg shadow-xl w-full max-w-xl p-8">
        <FileUploaderForm />
      </div>
    </div>
  );
}
