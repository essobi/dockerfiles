FROM ubuntu:16.04  
  
# Default config  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties \  
&& apt-get install -y openssh-server git subversion fakeroot language-pack-en-
base \  
&& apt-get install -y iputils-ping \  
&& apt-get install -y curl \  
&& apt-get install -y vim net-tools make \  
&& dpkg-reconfigure locales \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /var/run/sshd  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:e  
ENV LC_ALL en_US.UTF-8  
  
  
RUN add-apt-repository ppa:webupd8team/java && \  
add-apt-repository ppa:cwchien/gradle && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
  
# Oracle Java8, Gradle  
RUN apt-get update \  
&& apt-get install -y oracle-java8-installer oracle-java8-set-default \  
&& apt-get install -y gradle \  
&& ln -s /usr/lib/jvm/java-8-oracle/jre /usr/lib/jvm/default-java \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Docker daemon  
RUN apt-get update \  
&& apt-get install -y ca-certificates apt-transport-https \  
&& apt-key adv \  
\--keyserver hkp://ha.pool.sks-keyservers.net:80 \  
\--recv-keys 58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | tee
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual
\  
&& apt-cache policy docker-engine \  
&& apt-get install -y docker-engine \  
&& usermod -aG docker $(whoami)  
  
# Docker-compose  
RUN apt-get update \  
&& curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-
compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  
#GIT  
RUN apt-get install -y git \  
&& git config --global http.sslverify false  
  
#REDIS-TOOLS  
RUN apt-get install -y redis-tools  
  
#NMP  
RUN wget -qO- https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g npm  
  
CMD /bin/bash  
  
# TO RUN BUILD USE COMMAND: docker build -t bulf/ubuntu:1.0 .  

