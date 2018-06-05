FROM cybercode/alpine-ruby:2.2  
MAINTAINER yopp <rancher-localroute.github.com@yopp.in>  
  
ENV RANCHER_LOCALROUTE 0.2.0  
COPY iptables-poller iptables-poller  
  
RUN apk --update add iptables  
  
RUN chmod +x iptables-poller  
  
CMD ["iptables-poller"]  
ENTRYPOINT ["/usr/bin/ruby"]  

