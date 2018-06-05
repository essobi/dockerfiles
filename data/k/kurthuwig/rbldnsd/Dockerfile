FROM debian:stable  
  
MAINTAINER Kurt Huwig  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
rbldnsd \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
VOLUME ["/var/lib/rbldnsd"]  
  
WORKDIR /var/lib/rbldnsd  
  
ENTRYPOINT ["/usr/sbin/rbldnsd", "-b", "0.0.0.0", "-n"]  
  
EXPOSE 53/udp  

