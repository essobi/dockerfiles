FROM ubuntu:xenial  
  
MAINTAINER Nick Badal <me@nbad.al>  
  
# Silence apt warnings  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Setup ENV vars  
ENV STEAM_USERNAME="" \  
STEAM_PASSWORD="" \  
STEAM_GUARDCODE="" \  
PUID=1000 \  
PGID=1000  
# Copy scripts/configs  
COPY . /  
  
# Set up environment  
RUN apt-get update -qqy && apt-get install -qqy \  
curl \  
lib32gcc1 \  
sudo \  
&& groupadd -g 1000 starbound \  
&& useradd -u 1000 -g starbound starbound \  
&& mkdir -p \  
/steam \  
/starbound \  
&& chmod +x /setup.sh /run.sh  
  
VOLUME ["/starbound", "/steam"]  
  
EXPOSE 21025/tcp 21026/tcp  
  
WORKDIR /  
ENTRYPOINT ["/setup.sh"]  

