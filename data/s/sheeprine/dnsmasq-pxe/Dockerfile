FROM debian:jessie  
  
ENV RANGE_START=172.16.42.10  
ENV RANGE_END=172.16.42.100  
ENV RANGE_NETMASK=255.255.255.0  
ENV LEASE_TIME=1h  
ENV GATEWAY=172.16.42.1  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
dnsmasq \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework
/usr/bin/  
ADD entrypoint.sh /  
RUN chmod a+x /usr/bin/pipework  
  
VOLUME /var/lib/dnsmasq  
  
RUN touch /var/lib/dnsmasq/hosts  
RUN touch /var/lib/dnsmasq/options  
  
EXPOSE 53/udp  
ENTRYPOINT ["/entrypoint.sh"]  

