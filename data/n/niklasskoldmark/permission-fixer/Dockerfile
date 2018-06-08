FROM debian:8.1  
  
MAINTAINER Niklas Skoldmark <niklas.skoldmark@gmail.com>  
  
COPY ["entrypoint.sh", "/srv/entrypoint.sh"]  
  
ENV PERMISSION=777 LOG_ERROR_TO_CONSOLE=true  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install \  
-y \  
inotify-tools \  
&& \  
apt-get clean && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* \  
mkdir /watchdir \  
mkdir /logdir  
  
VOLUME /watchdir /logdir  
  
ENTRYPOINT ["/srv/entrypoint.sh"]

