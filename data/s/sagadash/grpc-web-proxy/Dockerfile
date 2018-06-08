FROM golang:alpine  
RUN apk add --no-cache git ca-certificates\  
&& rm -rf /var/lib/apt/lists/*  
  
RUN go get -v -u github.com/golang/dep/cmd/dep  
RUN go get -v github.com/improbable-eng/grpc-web/go/grpcwebproxy ; exit 0  
RUN cd src/github.com/improbable-eng/grpc-web && dep ensure  
RUN go get -v -u github.com/improbable-eng/grpc-web/go/grpcwebproxy  
  
ENTRYPOINT [ "/bin/sh", "-c", "exec /go/bin/grpcwebproxy
--server_tls_cert_file=$GRPCWEBPROXY_CERTIFICATE_KEY
\--server_tls_key_file=$GRPCWEBPROXY_PRIVATE_KEY
\--backend_tls=$GRPCWEBPROXY_BACKEND_TLS
\--backend_tls_noverify=$GRPCWEBPROXY_BACKEND_TLS_NOVERIFY
\--backend_addr=$GRPC_HOST:$GRPC_PORT
\--server_bind_address=$GRPCWEBPROXY_BIND
\--server_http_debug_port=$GRPCWEBPROXY_PORT
\--server_http_tls_port=$GRPCWEBPROXY_TLS_PORT
\--run_http_server=$GRPCWEBPROXY_RUN_HTTP
\--run_tls_server=$GRPCWEBPROXY_RUN_TLS
\--server_http_max_write_timeout=$GRPCWEBPROXY_WRITE_TIMEOUT
\--server_http_max_read_timeout=$GRPCWEBPROXY_READ_TIMEOUT" ]  

