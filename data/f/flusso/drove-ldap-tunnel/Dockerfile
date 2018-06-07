FROM ubuntu:16.04  
# Maintainer will be deprecates soon (1.13)  
MAINTAINER Lars van Mourik <l.vanmourik@flusso.nl>  
LABEL authors="Lars van Mourik <l.vanmourik@flusso.nl>, Joost van der Griendt
<j.vandergriendt@flusso.nl>"  
LABEL version="1.0.0"  
LABEL description="custom stunnel for drove"  
  
ENV OUTGOING_PORT="changeit"  
ENV OUTGOING_HOST="changeit"  
#### Stunnel  
RUN apt-get update && apt-get install --no-install-recommends -y
stunnel4=3:5.30-1 && rm -rf /var/lib/apt/lists/*  
  
COPY stunnel4 /etc/default/  
COPY stunnel.conf /etc/stunnel/  
COPY healthcheck.sh /etc/default  
  
HEALTHCHECK \--interval=30s CMD ["/bin/sh", "/etc/default/healthcheck.sh"]  
  
EXPOSE 389  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]

