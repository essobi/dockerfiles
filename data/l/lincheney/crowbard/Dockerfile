FROM alpine as builder  
  
ENV GOPATH=/build  
RUN apk add --no-cache git go build-base && \  
go get github.com/q3k/crowbar && \  
go build --ldflags '-w -linkmode external -extldflags "-static"'
github.com/q3k/crowbar/cmd/crowbard  
  
FROM scratch  
COPY \--from=builder /crowbard /bin/  
ENTRYPOINT ["crowbard"]  

