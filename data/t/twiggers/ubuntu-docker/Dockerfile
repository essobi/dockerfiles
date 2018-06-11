FROM ubuntu:rolling  
LABEL description="Ubuntu:rolling with Docker CE"  
MAINTAINER "Thom Wiggers <thom@thomwiggers.nl>"  
# Prevent configuration prompts  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update -qq && \  
apt-get install -qqy \  
apt-transport-https \  
lsb-release \  
curl && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \  
echo "deb https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
> \  
/etc/apt/sources.list.d/docker.list && \  
apt-get update -qq && \  
apt-get install -qqy docker-ce && \  
# Keep apt-transport-https to not break apt-get update  
apt-get remove -qqy \  
lsb-release \  
curl && \  
apt-get autoremove -qqy && \  
rm -rf /var/cache/apt/  
  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY modprobe.sh /usr/local/bin/modprobe  
  
# Reset frontend  
ENV DEBIAN_FRONTEND=  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

