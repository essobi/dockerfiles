FROM gregory90/base:latest  
  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get update  
  
# Install Varnish  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apt-transport-https  
RUN curl https://repo.varnish-cache.org/debian/GPG-key.txt | apt-key add -  
RUN echo "deb https://repo.varnish-cache.org/debian/ wheezy varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list  
RUN apt-get update  
RUN apt-get install -y varnish  
  
ADD default.vcl /etc/varnish/default.vcl  
  
ENV VARNISH_CACHE_SIZE 100M  
ENV VARNISH_BACKEND_PORT 3000  
ENV VARNISH_BACKEND_IP 172.17.42.1  
ENV VARNISH_PORT 80  
# Add scripts  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  

