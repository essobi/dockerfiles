FROM ubuntu:16.04  
  
ENV REALM_VERSION 1.0.3-231  
  
RUN \  
apt-get update && apt-get install -y curl && \  
curl -s https://packagecloud.io/install/repositories/realm/realm/script.deb.sh
| bash && \  
apt-get update && apt-get install -y realm-object-server-
developer=$REALM_VERSION && \  
systemctl enable realm-object-server && \  
apt-get autoremove -y curl && rm -rf /var/cache/apt/archives && \  
dpkg -s realm-object-server-developer  
  
EXPOSE 9080 9443  
  
VOLUME ["/var/lib/realm/object-server"]  
  
CMD ["/usr/bin/realm-object-server", "-c", "/etc/realm/configuration.yml"]  

