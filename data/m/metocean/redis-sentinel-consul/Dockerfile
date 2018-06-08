FROM redis  
MAINTAINER Troy Mare <t.mare@metocean.co.nz>  
  
ADD https://releases.hashicorp.com/consul/0.5.2/consul_0.5.2_linux_amd64.zip
/tmp/consul.zip  
ADD . /install/  
RUN /install/install.sh  
ENV GOMAXPROCS=2  
CMD ["/sbin/initsh"]  

