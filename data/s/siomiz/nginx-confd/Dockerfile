FROM nginx:latest  
  
MAINTAINER Tomohisa Kusano <siomiz@gmail.com>  
  
COPY copyables /  
  
ENV CONFD_VERSION 0.11.0  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 /opt/confd/confd  
  
RUN chmod +x /opt/confd/confd /entrypoint.sh  
  
VOLUME ["/etc/letsencrypt"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 443  
CMD ["/opt/confd/confd"]  

