FROM alpine:3.7 AS builder  
RUN apk add --no-cache curl  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/v1.9.0/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl  
  
FROM python:3-alpine  
RUN pip install awscli  
COPY \--from=builder /kubectl /usr/local/bin/kubectl  
RUN kubectl --help

