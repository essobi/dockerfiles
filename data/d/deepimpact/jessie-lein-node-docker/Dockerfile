FROM node:6.11.3-slim  
  
# Add `backports` repos - refer to https://backports.debian.org  
RUN echo 'deb http://ftp.de.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list \  
&& echo 'deb http://http.debian.net/debian wheezy-backports main' >>
/etc/apt/sources.list  
  
# Install base packages  
RUN apt-get update \  
&& apt-get install -y autoconf curl git libpng-dev libtool nasm sudo libelf1 \  
&& apt-get install -y libyaml-dev openssh-client python-dev python-pip zip \  
&& apt-get install -y -t jessie-backports openjdk-8-jdk-headless  
  
# Install git lfs  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | sudo bash \  
&& apt install -y git-lfs \  
&& git lfs install  
  
# Install awscli  
RUN pip install awscli  
  
# Install docker  
RUN VER="17.05.0-ce" \  
&& curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$VER.tgz \  
&& mv /tmp/docker/* /usr/bin  
  
# Add user `bmo`  
RUN useradd --create-home -m bmo -G sudo \  
&& adduser bmo sudo \  
&& echo "bmo:bmo" | chpasswd  
  
# Install Leiningen  
RUN curl --silent
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/usr/local/bin/lein \  
&& chmod +x /usr/local/bin/lein \  
&& su bmo -c "lein"  
  
# Install wscat  
RUN npm install -g wscat  
  
# Enable passwordless sudo for users under the "sudo" group  
RUN sed -i.bkp -e 's/%sudo\s\\+ALL=(ALL\\(:ALL\\)\?)\s\\+ALL/%sudo
ALL=NOPASSWD:ALL/g' /etc/sudoers  
  
# Cleanup  
RUN rm -rf /tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
# Start as a non-root user  
USER bmo  
  

