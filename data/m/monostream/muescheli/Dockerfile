FROM golang:1.9-alpine as builder  
  
RUN apk add --update --no-cache ca-certificates  
  
# build  
WORKDIR /go/src/github.com/monostream/muescheli/  
  
COPY . .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o muescheli .  
  
# copy artefacts  
WORKDIR /app/  
RUN cp /go/src/github.com/monostream/muescheli/muescheli .  
RUN rm -r /go/src/  
  
FROM scratch  
  
# copy certificates so that files can be fetched from ssl sites  
COPY \--from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
  
# setup environment  
WORKDIR /app/  
ENV PATH "/app:${PATH}"  
# add non-privileged user  
COPY passwd.minimal /etc/passwd  
USER nobody  
  
COPY \--from=builder /app/ .  
  
CMD ["muescheli"]  

