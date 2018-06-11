FROM vertigo/docker-base  
  
MAINTAINER Andre Fernandes <andre@vertigo.com.br>  
  
ARG BASEREPO  
ARG EPELREPO  
  
ADD src/nginx.repo /etc/yum.repos.d/nginx.repo  
  
RUN /opt/setbaserepo.sh && \  
/opt/setepelrepo.sh && \  
yum update -y && \  
yum install nginx -y && \  
yum clean all  
RUN yum install python-pip gcc libffi libffi-devel python-devel openssl-devel
dialog cronie -y && \  
pip install letsencrypt && \  
yum clean all  
  
ADD src/entrypoint.sh /entrypoint.sh  
ADD src/templates /templates  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
chmod +x /entrypoint.sh && \  
mkdir -p /etc/letsencrypt/webrootauth  
  
EXPOSE 80 443  
CMD ["/entrypoint.sh"]  

