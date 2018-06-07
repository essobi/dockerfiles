FROM golang:1.10-alpine  
  
RUN apk add --no-cache --update alpine-sdk protobuf protobuf-dev  
  
COPY . /go/src/github.com/nlnwa/maalfrid-language-detector  
RUN cd /go/src/github.com/nlnwa/maalfrid-language-detector && make release-
binary  
  
FROM scratch  
LABEL maintainer="nettarkivet@nb.no"  
COPY \--from=0 /go/src/github.com/nlnwa/maalfrid-language-detector/maalfrid /  
ENV COUNT=5 PORT=8672 MAX_RECV_MSG_SIZE=10000000  
EXPOSE 8672  
ENTRYPOINT ["/maalfrid"]  
CMD ["serve"]  

