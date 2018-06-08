FROM ubuntu:16.04  
MAINTAINER Michael Sauter <mail@michaelsauter.net>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update -qq -y; \  
apt-get install -y apt-utils  
  
RUN apt-get install -y \  
sudo \  
curl \  
iputils-ping \  
build-essential \  
autoconf \  
tzdata \  
locales \  
apt-transport-https  
  
RUN echo Europe/Berlin > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN locale-gen en_US.UTF-8  
ENV LANG="en_US.UTF-8" LANGUAGE="en_US:en" LC_ALL="en_US.UTF-8"
LC_CTYPE="en_US.UTF-8"  
RUN useradd -m -s /bin/bash ubuntu; \  
chgrp -R ubuntu /usr/local; \  
find /usr/local -type d | xargs chmod g+w; \  
echo "ubuntu ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/ubuntu; \  
chmod 0440 /etc/sudoers.d/ubuntu  
  
ADD bin/dumb-init_1.2.0 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
ENV DUMB_INIT_SETSID 0  
ENV HOME /home/ubuntu  
WORKDIR /home/ubuntu  
USER ubuntu  
ENTRYPOINT ["dumb-init"]

