FROM golang:onbuild  
ADD . /root/  
WORKDIR /root  
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -v -x ec2-testing.go &&
chmod +x ec2-testing  
  
FROM alpine:latest  
WORKDIR /root  
COPY \--from=0 /root/ec2-testing .  
RUN echo "builded date: $(date -u)" > date.txt  
EXPOSE 8080  
CMD ["./ec2-testing"]  

