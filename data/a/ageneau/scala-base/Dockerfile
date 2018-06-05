FROM ageneau/devel-base:latest  
  
MAINTAINER Sylvain Ageneau <ageneau@gmail.com>  
  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main contrib
non-free" | tee -a /etc/apt/sources.list.d/jessie-backports.list  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
RUN apt-get update  
RUN apt-get -t jessie-backports install -y --no-install-recommends
openjdk-8-jdk  
RUN apt-get install -y --no-install-recommends sbt \  
npm \  
closure-compiler  
RUN apt-get install -y --no-install-recommends git \  
zsh \  
wget \  
curl \  
locales \  
less  
RUN apt-get clean && apt-get autoclean  
  
# `npm` relies on a `node` executable, but we have `nodejs`.  
# https://github.com/joyent/node/issues/3911  
RUN ln -sf '/usr/bin/nodejs' '/usr/bin/node'  
  
# Installed `npm` is too old, upgrade it.  
RUN npm update -g  
RUN npm install -g npm  
RUN npm install -g gulp  
RUN npm install -g svgo  
  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
  
WORKDIR /project  
  
ENV LC_ALL C.UTF-8  
ENV JAVA_OPTS="-Xms64M -Xmx3072M -Xss4M -XX:ReservedCodeCacheSize=64m
-XX:+CMSClassUnloadingEnabled -XX:+UseConcMarkSweepGC"  
CMD ["sbt", "run"]  
  

