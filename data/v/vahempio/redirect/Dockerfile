FROM golang:1.10.0  
WORKDIR /myapp  
COPY app.go .  
RUN CGO_ENABLED=0 go build -a --installsuffix cgo --ldflags="-s" -o
bin/redirect  
  
FROM scratch  
LABEL maintainer="vahempio@gmail.com"  
COPY \--from=0 /myapp/bin/redirect /  
ENTRYPOINT ["/redirect"]  
EXPOSE 80  

