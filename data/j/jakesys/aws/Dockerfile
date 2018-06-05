FROM alpine:latest  
MAINTAINER Jake Buchholz <jakesys@jakesys.net>  
  
COPY root .version /  
RUN /bootstrap.sh  
  
ENTRYPOINT ["/usr/bin/aws"]  
CMD ["--version"]  
  
VOLUME ["/root/.aws"]  

