FROM golang:1.10-alpine3.7 AS builder  
RUN apk add \--no-cache git gcc g++  
RUN go get -v github.com/rubenv/sql-migrate/sql-migrate  
  
FROM alpine:3.7  
COPY \--from=builder /go/bin/sql-migrate /bin/sql-migrate

