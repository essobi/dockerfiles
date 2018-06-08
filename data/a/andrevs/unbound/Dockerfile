FROM debian  
  
MAINTAINER Andre van Schalkwyk "andre@hebe.ch"  
# Unbound  
#RUN apk add --update unbound ; \  
# apk add --update curl; \  
# rm -rf /var/cache/apk/* ;  
RUN apt-get update && \  
apt-get install -y iptables unbound curl && \  
apt-get clean && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/unbound/etc  
RUN curl -s -o /var/unbound/etc/root.hints
ftp://ftp.internic.net/domain/named.cache  
  
COPY unbound.conf /etc/unbound/unbound.conf  
COPY root.key /var/unbound/etc/root.key  
COPY unbound_custom.conf /etc/unbound/unbound_custom.conf  
COPY unbound_hosts.conf /etc/unbound/unbound_hosts.conf  
  
EXPOSE 53/udp  
  
RUN unbound-checkconf  
  
# start stuff  
#RUN curl -sk
http://freedns.afraid.org/dynamic/update.php?SG43dW8xMTBZY2xTR0hSenBFV3o6MTAwNjA4NTQ=  
CMD unbound  

