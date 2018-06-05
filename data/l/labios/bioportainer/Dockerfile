FROM alpine:latest  
  
RUN apk --update upgrade && apk add ca-certificates bash && rm -rf
/var/cache/apk/*  
  
COPY bioportainer /  
VOLUME /data  
WORKDIR /  
EXPOSE 9000  
ENTRYPOINT ["/bioportainer"]  

