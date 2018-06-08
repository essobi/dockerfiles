FROM scratch  
ADD bin /bin  
ADD lib /lib  
ADD usr /usr  
RUN /bin/busybox --install -s /bin  
ADD docker-entrypoint.sh /bin/link-manager  
  
LABEL org.label-schema.name="DHCP Client for Docker Containers" \  
org.label-schema.description="This container runs a dhcp client and manages
the network interfaces." \  
org.label-schema.url="https://github.com/steigr/docker-link-manager" \  
org.label-schema.vcs-url="https://github.com/steigr/docker-link-manager" \  
org.label-schema.vendor="Mathias Kaufmann" \  
org.label-schema.version="2" \  
org.label-schema.schema-version="1.0"  
  
ENTRYPOINT ["link-manager"]

