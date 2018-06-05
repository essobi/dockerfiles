# build stage  
FROM golang AS build-env  
WORKDIR /go/src/github.com/emaildanwilson/cf-vault-service-broker  
ADD . .  
RUN go get . && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix nocgo -o
/app  
  
# final stage  
FROM centurylink/ca-certs  
COPY \--from=build-env /app /  
EXPOSE 8000  
CMD ["/app"]

