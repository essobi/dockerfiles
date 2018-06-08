FROM debian:jessie  
MAINTAINER Shawn Nock <nock@nocko.se>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
unbound && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
COPY quakecon.conf /etc/unbound/unbound.conf.d/  
  
ENV AUTHORITATIVE_ZONES "at.quakecon.org. \  
quakeconcdn.org. \  
16.172.in-addr.arpa. \  
17.172.in-addr.arpa. \  
18.172.in-addr.arpa. \  
19.172.in-addr.arpa. \  
20.172.in-addr.arpa. \  
21.172.in-addr.arpa. \  
22.172.in-addr.arpa."  
ENV AUTHORITATIVE_SERVERS "172.17.1.102@5353 \  
172.17.1.103@5353 \  
172.17.1.104@5353"  
COPY run.sh /  
RUN chmod +x /run.sh  
  
cmd ["/run.sh"]  

