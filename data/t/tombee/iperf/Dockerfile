FROM alpine:3.6  
LABEL maintainer "Tom Barlow <tom.barlow@docker.com>"  
  
RUN apk add --update \  
iperf3 && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 5201  
ENTRYPOINT ["iperf3"]  

