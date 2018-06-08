FROM golang:latest  
WORKDIR /go/src/bitbucket.com/the_mouldiwarp/sslcheck-api  
ADD ./go_source/* ./  
RUN GOOS=linux GOARCH=arm GOARM=5 go build -o sslcheck-api .  
  
FROM ubuntu:latest  
RUN useradd -u 10001 nonroot  
  
FROM scratch  
ENV PEMPATH=/etc/ssl/certs/custom/custom.pem  
ENV KEYPATH=/etc/ssl/certs/custom/custom.key  
COPY \--from=0 /go/src/bitbucket.com/the_mouldiwarp/sslcheck-api/sslcheck-api
/bin/sslcheck  
COPY \--from=1 /etc/passwd /etc/passwd  
COPY /useless_ssl/* /etc/ssl/certs/custom/  
EXPOSE 8443  
USER nonroot  
ENTRYPOINT ["/bin/sslcheck"]  

