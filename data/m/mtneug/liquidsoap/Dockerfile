FROM debian:jessie  
MAINTAINER Matthias Neugebauer <mtneug@mailbox.org>  
  
RUN groupadd -r liquidsoap --gid=888 && useradd -r -g liquidsoap --uid=888
liquidsoap  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
liquidsoap liquidsoap-plugin-all \  
&& rm -rf /var/lib/apt/lists/*  
  
USER liquidsoap  
EXPOSE 8005  
CMD ["liquidsoap", "--interactive"]  

