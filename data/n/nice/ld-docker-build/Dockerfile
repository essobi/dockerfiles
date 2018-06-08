FROM debian:wheezy  
MAINTAINER Ryan Roberts <ryansroberts@gmail.com>  
  
  
RUN echo "deb http://http.debian.net/debian wheezy-backports main"
>/etc/apt/sources.list.d/wheezy-backports.list  
  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/3.12.0
main" | tee /etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get update -y  
  
RUN apt-get install -y \  
sudo \  
mono-complete \  
libtool \  
autoconf \  
g++ \  
gettext \  
openjdk-7-jre-headless \  
make \  
cmake \  
wget \  
htop \  
pandoc \  
haskell-platform  
  
  
RUN sudo apt-get -t wheezy-backports install -y git mercurial  
  
RUN apt-get install -y apt-utils  
RUN apt-get install -y fsharp  
  
#RUN apt-get install -y nodejs npm mono-complete &&\  
# npm install -g grunt &&\  
# ln /usr/bin/nodejs /usr/bin/node  
  
RUN apt-get install curl &&\  
curl --silent \--location https://deb.nodesource.com/setup_4.x | bash - &&\  
apt-get install --yes nodejs &&\  
apt-get install mono-complete  
  
RUN mozroots --import --sync &&\  
yes | certmgr --ssl -m https://go.microsoft.com &&\  
yes | certmgr -ssl -m https://nugetgallery.blob.core.windows.net &&\  
yes | certmgr -ssl -m https://nuget.org  

