FROM haproxy:latest  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends curl ca-certificates cron \  
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD proxyfile-generate.sh /proxyfile-generate.sh  
ADD proxy-list.sh /proxy-list.sh  
RUN ln -s /proxyfile-generate.sh /etc/cron.daily/proxyfile-generate.sh  
  
ENTRYPOINT ["/proxy-list.sh"]  
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]  

