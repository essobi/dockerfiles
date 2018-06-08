FROM fizzy33/a8_base_image:latest  
  
MAINTAINER Glen Marchesani "https://github.com/fizzy33"  
RUN \  
add-apt-repository ppa:haxe/releases -y && \  
apt-add-repository -y ppa:andrei-pozolotin/maven3 && \  
apt-get update && \  
apt-get install -y haxe maven3 && \  
mkdir ~/haxelib && haxelib setup ~/haxelib  
  
RUN mkdir -p /usr/local/_packages  
  
WORKDIR /usr/local/_packages  
  
# install zinc  
RUN \  
wget http://downloads.typesafe.com/zinc/0.3.7/zinc-0.3.7.tgz && \  
tar xf zinc-0.3.7.tgz && \  
rm zinc-0.3.7.tgz  
  
# install phantomjs  
WORKDIR /usr/local/share/  
ENV PHANTOM_JS phantomjs-1.9.8-linux-x86_64  
RUN \  
apt-get install -y build-essential chrpath libssl-dev libxft-dev libfreetype6
libfreetype6-dev libfontconfig1 libfontconfig1-dev && \  
wget https://bitbucket.org/ariya/phantomjs/downloads/${PHANTOM_JS}.tar.bz2 &&
\  
tar xvjf ${PHANTOM_JS}.tar.bz2 && \  
ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin && \  
rm ${PHANTOM_JS}.tar.bz2  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
  
COPY image/ /  
  
WORKDIR /root/  
  
CMD ["/sbin/my_init"]  
  
#  
# possibly  
# scala  
# imm (scala repl)  
#  
# == build with ==  
#  
# docker build -t a8_java_dev .  

