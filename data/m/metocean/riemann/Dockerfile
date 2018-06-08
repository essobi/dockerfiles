FROM metocean/aroha:v1.0.0  
MAINTAINER Thomas Coats <thomas@metocean.co.nz>  
  
ENV RIEMANN_VERSION=0.2.10  
ADD . /install/  
RUN /install/install.sh  
CMD ["/sbin/initsh"]

