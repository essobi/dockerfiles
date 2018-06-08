FROM gliderlabs/alpine:latest  
  
MAINTAINER Carlos León <mail@carlosleon.info>  
  
RUN apk-install darkhttpd  
  
EXPOSE 80  
ENTRYPOINT ["/usr/bin/darkhttpd"]  
  
CMD ["/var/www", "--chroot"]  

