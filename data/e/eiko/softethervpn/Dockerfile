FROM centos:centos7  
  
ENV BUILD_VERSION v4.25-9656-rtm  
  
COPY copyables /  
RUN chmod +x /entrypoint.sh /gencert.sh  
  
RUN bash /build.sh \  
&& rm /build.sh  
  
WORKDIR /opt  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 500/udp 4500/udp 1701/tcp 1194/udp 5555/tcp  
  
CMD ["/usr/local/bin/dumb-init", "--", "/opt/vpnserver", "execsvc"]  

