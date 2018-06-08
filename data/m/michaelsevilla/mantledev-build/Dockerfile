FROM ivotron/cephdev-build:latest  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y lua5.2 liblua5.2-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* debian/  
  
ADD build /  
RUN chmod 755 /build  
ENTRYPOINT ["/build"]  

