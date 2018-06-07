FROM jarfil/salt-master-docs:debian-buster  
  
MAINTAINER Jaroslaw Filiochowski <jarfil@gmail.com>  
  
COPY docker-entrypoint.sh /  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
salt-api \  
salt-proxy \  
salt-syndic && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
RUN chmod +x \  
/docker-entrypoint.sh  
  
EXPOSE 4505 4506  
  
CMD /docker-entrypoint.sh  

