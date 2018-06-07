FROM debian:jessie  
MAINTAINER Matthias Neugebauer <mtneug@mailbox.org>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
icecast2 \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY icecast.xml /etc/icecast2/icecast.xml  
RUN chown icecast2:icecast /etc/icecast2/icecast.xml  
  
USER icecast2  
  
EXPOSE 8000  
CMD ["icecast2", "-c", "/etc/icecast2/icecast.xml"]  

