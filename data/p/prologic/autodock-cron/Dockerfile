# Build  
FROM golang:alpine AS build  
  
ENV PLUGIN autodock-cron  
  
RUN apk add --update git make build-base && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /go/src/${PLUGIN}  
COPY . /go/src/${PLUGIN}  
RUN make build  
  
# Runtime  
FROM scratch  
  
ENV PLUGIN autodock-cron  
  
LABEL autodock.app main  
  
COPY \--from=build /go/src/${PLUGIN}/${PLUGIN} /${PLUGIN}  
  
ENTRYPOINT ["/autodock-cron"]  
CMD []  

