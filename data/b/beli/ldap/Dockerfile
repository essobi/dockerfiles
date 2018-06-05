FROM debian:stretch  
MAINTAINER Michal Belica <devel@beli.sk>  
  
EXPOSE 389  
# runs as user openldap(104), group openldap(107)  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
slapd ldap-utils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
COPY entrypoint /  
RUN chmod 0755 /entrypoint \  
&& rm -r /var/lib/ldap \  
&& mkdir /config \  
&& mkdir /data \  
&& mkdir /initdb.d \  
&& chown openldap:openldap /config /data \  
&& ln -s /data /var/lib/ldap  
VOLUME /data  
VOLUME /config  
CMD ["/entrypoint"]  

