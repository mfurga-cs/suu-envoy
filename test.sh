echo "ENVOY test"

echo -e "\n\nHTTP service-1:"
curl 127.0.0.1:8000/service-1/endpoint-1
echo -e "\n\nHTTP service-2:"
curl 127.0.0.1:8000/service-2/endpoint-1
echo -e "\n\nHTTP service-3:"
curl 127.0.0.1:8000/service-3/endpoint-1

echo -e "\n"

echo -e "\ngRPC service-1:"
grpcurl -plaintext -proto grpc-services/info.proto 127.0.0.1:10000 suu.Test1/Info1
echo -e "\ngRPC service-2:"
grpcurl -plaintext -proto grpc-services/info.proto 127.0.0.1:10000 suu.Test2/Info2
echo -e "\ngRPC service-3:"
grpcurl -plaintext -proto grpc-services/info.proto 127.0.0.1:10000 suu.Test3/Info3

echo -e "\nPostgres service:"
echo "SELECT * FROM cars;" | \
	PGPASSWORD=envoy psql -h 127.0.0.1 -p 12000 -U envoy --dbname=envoy
