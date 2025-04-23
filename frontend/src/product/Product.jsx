import React, { useEffect, useState } from 'react';

export default function Product() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    async function getdata() {
      let res = await fetch("http://127.0.0.1:8000/api/product/");
      let data = await res.json();
      setProducts(data);
    }
    getdata();
  }, []);

  return (
    <div className="bg-white">
      <div className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
        <h2 className="text-2xl font-bold tracking-tight text-gray-900">
          Customers also purchased
        </h2>

        <div className="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
          {products.map((product) => (
            <div key={product.id} className="group relative">
              <img
                alt={product.product_name}
                src={`http://127.0.0.1:8000${product.product_image}`}
                className="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80"
              />
              <div className="mt-4 flex justify-between">
                <div>
                  <h3 className="text-sm text-gray-700">{product.product_name}</h3>
                  <p className="mt-1 text-sm text-gray-500">{product.product_bio}</p>
                </div>
                <p className="text-sm font-medium text-gray-900">₹{product.product_price}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
