# Periodic rsync copy jobs  
FROM debian:jessie  
MAINTAINER gw0 [http://gw.tnode.com/] <gw.2016@tnode.com>  
  
# install debian packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq \  
&& apt-get install --no-install-recommends -y \  
cron \  
rsync \  
openssh-client \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# remove default cron jobs  
RUN rm -f /etc/cron.*/*  
  
# expose  
#VOLUME /etc/cron.d  
#VOLUME /root/.ssh  
#VOLUME /data  
CMD ["cron", "-f"]  

