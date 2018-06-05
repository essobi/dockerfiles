FROM ubuntu:16.04  
MAINTAINER jerome.petazzoni@docker.com  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq \  
&& apt-get install -qqy \  
build-essential \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables \  
make \  
tmux \  
python \  
&& curl -sSL https://get.docker.com | sh \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# libnss-resolver  
ENV LIBNSS_VERSION 0.3.0  
RUN curl -L https://github.com/azukiapp/libnss-
resolver/releases/download/v${LIBNSS_VERSION}/ubuntu14-libnss-
resolver_${LIBNSS_VERSION}_amd64.deb -o /tmp/libnss-resolver.deb \  
&& dpkg -i /tmp/libnss-resolver.deb  
  
# Install the magic wrapper.  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
CMD ["wrapdocker"]  

