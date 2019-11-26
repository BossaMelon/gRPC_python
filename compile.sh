mkdir compiled

python -m grpc_tools.protoc -I. --python_out=./compiled --grpc_python_out=./compiled first.proto

echo "OK!"