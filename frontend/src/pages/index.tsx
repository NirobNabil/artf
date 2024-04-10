import FileUploaderForm from "../../components/FileUploadForm";
import Link from "next/link";

export default function Page() {
  return (
    <div className="bg-gray-900 min-h-screen flex flex-col justify-center items-center p-8">
      <Link href={"/supplier"}>Supplier</Link>
      <Link href={"/buyer"}>Buyer</Link>
    </div>
  );
}
