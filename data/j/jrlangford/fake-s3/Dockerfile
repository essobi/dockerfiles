FROM debian:jessie  
MAINTAINER jonathan.langford@schibsted.com.mx  
  
RUN apt-get update && \  
apt-get install -y ruby rubygems-integration  
  
RUN gem install fakes3  
  
ENTRYPOINT ["/usr/local/bin/fakes3"]  
CMD ["-r", "/mnt/fakes3_root", "-p", "4567"]  
  
EXPOSE 4567  

