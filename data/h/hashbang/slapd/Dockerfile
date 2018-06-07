FROM debian:jessie  
  
RUN apt-get update && \  
LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ldap-utils \  
slapd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD run.sh /tmp/run.sh  
  
VOLUME /var/lib/ldap  
VOLUME /etc/ldap/slapd.d  
  
ENV ADMIN_PASS somepass  
ENV ROOT_PASS somepass  
ENV DOMAIN hashbang.sh  
ENV ORG Hashbang  
  
EXPOSE 389  
# Default command to run on boot  
CMD ["bash","/tmp/run.sh"]  

