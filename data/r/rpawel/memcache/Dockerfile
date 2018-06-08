FROM rpawel/ubuntu:trusty  
  
## START  
RUN apt-get -q -y update \  
&& apt-get dist-upgrade -y --no-install-recommends \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y -q memcached \  
&& DEBIAN_FRONTEND=newt  
  
ADD build.sh /  
ADD run.sh /  
  
## START  
RUN chmod +x /build.sh /run.sh \  
&& bash /build.sh && rm -f /build.sh  
  
ADD ./config /etc/  
  
# PORTS  
EXPOSE 11211  
  
ENTRYPOINT ["/run.sh"]  

