FROM debian:jessie  
MAINTAINER leef  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install Ruby  
RUN apt-get update && apt-get install -yqq ruby rubygems-integration  
  
# install fake-s3  
RUN gem install fakes3 -v 0.1.6.0  
  
# run fake-s3  
RUN mkdir -p /fakes3_root  
ENTRYPOINT ["/usr/local/bin/fakes3"]  
CMD ["-r", "/fakes3_root", "-p", "4569", "-h", "0.0.0.0"]  
EXPOSE 4569  

