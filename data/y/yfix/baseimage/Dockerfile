FROM ubuntu:16.04  
  
MAINTAINER Yuri Vysotskiy (yfix) <yfix.dev@gmail.com>  
  
ENV DEBIAN_FRONTED=noninteractive  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update && DEBIAN_FRONTED=noninteractive apt-get install -y
--reinstall \  
cron \  
inotify-tools \  
supervisor \  
curl \  
wget \  
dnsutils \  
net-tools \  
libc-bin \  
locales \  
\  
&& rm /bin/sh && ln -s /bin/bash /bin/sh \  
\  
&& locale-gen en_US en_US.UTF-8 \  
\  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY docker /  
  
WORKDIR /etc/supervisor/conf.d  
  
CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  

