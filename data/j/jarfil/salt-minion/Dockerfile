FROM jarfil/salt-common:debian-stretch  
  
MAINTAINER Jaroslaw Filiochowski <jarfil@gmail.com>  
  
COPY docker-entrypoint.sh /  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
salt-minion && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
RUN chmod +x \  
/docker-entrypoint.sh  
  
CMD /docker-entrypoint.sh  

