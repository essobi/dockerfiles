FROM phusion/baseimage  
MAINTAINER Ryan Roberts <ryansroberts@gmail.com>  
  
ENV JRE=jre1.8.0_60  
  
RUN apt-get update && apt-key adv --keyserver pgp.mit.edu --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
  
RUN echo "deb http://download.mono-project.com/repo/debian
wheezy/snapshots/3.12.0 main" > /etc/apt/sources.list.d/mono-xamarin.list &&\  
apt-get update &&\  
apt-get install -yy wget libc6 &&\  
#Java stuffs for stardog binaries  
wget http://www.java.net/download/jdk8u60/archive/b18/binaries/jre-8u60-ea-
bin-b18-linux-x64-02_jun_2015.tar.gz -O /tmp/${JRE}.tgz && \  
cd /opt && tar zxvf /tmp/${JRE}.tgz && \  
ln -s /opt/${JRE} /opt/jre && \  
ln -s /opt/jre/bin/java /usr/bin/java && \  
rm -rf /tmp/* &&\  
apt-get install -yy mono-devel ca-certificates-mono fsharp mono-vbnc nuget &&\  
apt-get install -yy git graphviz raptor-utils python make g++ inotify-tools
pandoc nodejs npm &&\  
npm install -g grunt &&\  
ln /usr/bin/nodejs /usr/bin/node &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

