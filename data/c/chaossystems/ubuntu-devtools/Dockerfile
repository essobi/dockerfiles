FROM ubuntu:17.10  
MAINTAINER Greg Orzell <chaos@chaossystems.io>  
  
ARG SCALA_VERSION=2.12.4  
ARG USER=root  
ARG HOME=/root  
  
# Base Packages  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
# Tools  
apt-utils \  
curl \  
dirmngr \  
fish \  
lsb-release \  
make \  
sudo \  
tmux \  
traceroute \  
vim \  
wget \  
# Development tools  
git \  
openjdk-9-jdk \  
gradle \  
nodejs \  
npm \  
python \  
python-pip \  
ruby \  
silversearcher-ag && \  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
# Scala Tools  
RUN wget
https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.deb
&& \  
dpkg -i scala-$SCALA_VERSION.deb && \  
curl -Lso /usr/local/bin/amm
https://github.com/lihaoyi/Ammonite/releases/download/1.0.3/2.12-1.0.3 && \  
chmod +x /usr/local/bin/amm && \  
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \  
apt-get update && \  
apt-get install sbt && \  
apt-get clean  
  
RUN if [ "$USER" != "root" ]; then \  
useradd -ms /usr/bin/fish $USER; \  
usermod $USER -a -G wheel; \  
sed -i 's/# %wheel/%wheel/' /etc/sudoers; \  
fi  
  
USER $USER:$USER  
WORKDIR $HOME  
CMD ["/usr/bin/tmux"]  

