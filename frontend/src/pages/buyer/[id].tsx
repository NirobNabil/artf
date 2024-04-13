import { useRouter } from "next/router";
import { useEffect, useState } from "react";

export default function Page() {

    const [productDetails, setProductDetails] = useState({})
    const [queryId, setQueryId]  = useState()
    const router = useRouter()
    const server_url = "http://localhost:8080/"

    useEffect( () => {
        if( !router.query.id ) return;

        console.log(router.query)

        fetch( server_url + 'product/' + router.query.id ).then( res => res.json() ).then( res => {
            setProductDetails(res)
        } )
    }, [router.query] )

  return (
    <div className="bg-gray-900 min-h-screen flex flex-col justify-center items-center p-8">
        <h1 className="text-6xl font-bold text-white text-left mb-8 opacity-70 w-full">
            Requested Product
        </h1>
        <div className="max-w-sm bg-gray-400 border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
            <a href="#">
                <img className="rounded-t-lg" src={server_url + productDetails['thumbnail']} alt="Product image" />
            </a>
            <div className="p-5">
                <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{productDetails['productName']}</h5>
                <h6 className="mb-2 text-sm tracking-tight text-gray-900 dark:text-white">{productDetails['id']}</h6>
                <h6 className="mb-2 text-md font-bold tracking-tight text-gray-900 dark:text-white">{`${productDetails['height']} x ${productDetails['width']}`}</h6>
                <a href="#" className="inline-flex items-center mt-4 px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Open in App
                    <svg className="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 5h12m0 0L9 1m4 4L9 9"/>
                    </svg>
                </a>
            </div>
        </div>
    </div>

  );
}
