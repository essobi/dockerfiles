FROM metocean/aroha:v1.0.0  
MAINTAINER Thomas Coats <thomas@metocean.co.nz>  
  
ENV ELASTICSEARCH_VERSION=2.3.1  
ADD . /install/  
RUN /install/install.sh  
CMD ["/sbin/initsh"]

