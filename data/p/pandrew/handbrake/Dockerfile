FROM alpine:edge  
  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
  
ENV HANDBRAKE_VERSION=0.10.2-r4  
RUN apk update \  
&& apk add handbrake=$HANDBRAKE_VERSION \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /data  
ENTRYPOINT ["HandBrakeCLI"]  
CMD ["-h"]  
  

