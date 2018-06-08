# --- ekino/puppetlabs:sid ---  
FROM debian:sid  
MAINTAINER Matthieu Fronton <fronton@ekino.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# prerequisites  
RUN apt-get update  
RUN apt-get install -y wget lsb-release apt-utils ca-certificates  
  
# puppet  
RUN wget -nv https://apt.puppetlabs.com/puppetlabs-release-$(lsb_release
-cs).deb  
RUN dpkg -i puppetlabs-release-$(lsb_release -cs).deb  
RUN apt-get update && apt-get install -y puppet  
RUN rm puppetlabs-release-$(lsb_release -cs).deb  
RUN gem install deep_merge  
  
# cleanup  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

