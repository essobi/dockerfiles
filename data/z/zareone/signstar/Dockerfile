FROM ubuntu:14.04  
RUN apt-get update  
  
RUN apt-get -y install openssl  
  
COPY mkcerts /bin/  
  
VOLUME ["/output"]  
  
WORKDIR /output  
  
ENTRYPOINT ["/bin/mkcerts"]  
  
CMD ["your.domain.here.com"]

