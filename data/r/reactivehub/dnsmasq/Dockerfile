FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DNSMASQ_VERSION 2.72  
ENV DNSMASQ_DEB_VERSION 2.72-3  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends dnsmasq=${DNSMASQ_DEB_VERSION}
\  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 53 53/udp  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["dnsmasq"]  

