FROM hpess/chef:latest  
MAINTAINER Karl Stoney <karl@jambr.co.uk>  
  
# Install pre-reqs  
RUN yum -y install git-core && \  
yum -y clean all  
  
RUN cd /opt && \  
git clone \--depth=1 https://github.com/rembo10/headphones.git && \  
chown -R docker:docker /opt/headphones  
  
EXPOSE 8181  
ENV chef_node_name headphones.docker.local  
  
COPY services/* /etc/supervisord.d/  
COPY preboot/* /preboot/  

