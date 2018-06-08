FROM mysql:latest  
MAINTAINER 7kbird <7kbird@gmail.com>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y curl  
  
# Install Stable Salt  
RUN curl -L https://bootstrap.saltstack.com -o install_salt.sh  
  
# Salt install script uses runlevel (which is unknown) to help determine if
packages are installed  
# This is a hack so installation will complete  
RUN ln -s /etc/rc2.d/ /etc/rc.d  
  
RUN sh install_salt.sh -D -X git v2014.7.5  
  
COPY salt-minion-entrypoint.sh /salt-minion-entrypoint.sh  
ENTRYPOINT ["sh", "/salt-minion-entrypoint.sh"]  
CMD ["/etc/salt"]

