# Build the application  
FROM golang:1.10.1 as build  
WORKDIR /go/  
  
RUN go get github.com/lib/pq  
RUN go get github.com/go-sql-driver/mysql  
RUN go get github.com/gocql/gocql  
RUN go get github.com/golang-migrate/migrate/cli  
  
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags "-s" -a
-installsuffix cgo -tags 'postgres cassandra redshift mysql aws-s3' -o migrate
github.com/golang-migrate/migrate/cli  
  
# Copy it into the base image.  
FROM gcr.io/distroless/base  
LABEL maintainer="xbasty@gmail.com"  
COPY \--from=build /go/migrate /  
ENTRYPOINT ["/migrate"]  

