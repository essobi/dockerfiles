FROM ubuntu:16.04  
  
RUN echo "deb http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu
xenial main " > /etc/apt/sources.list.d/handbreak.list \  
&& apt-get update \  
&& apt-get install --allow-unauthenticated -y handbrake-cli  
  
RUN useradd -u 1010 -U -d /config -s /bin/false abc && \  
usermod -G users abc  
  
# add local files  
COPY root/ /  
  
VOLUME /config  
VOLUME /input  
VOLUME /output  
  
USER abc  
ENTRYPOINT ["HandBrakeCLI"]  

