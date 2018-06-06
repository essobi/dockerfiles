FROM gcr.io/google_containers/ubuntu-slim:0.4  
MAINTAINER Shingo Omura <everpeace@gmail.com>  
  
# Disable prompts from apt.  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y &&\  
apt-get install -y --no-install-recommends curl jq bash && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
CMD ["tail", "-F", "-n0", "/etc/hosts" ]  

