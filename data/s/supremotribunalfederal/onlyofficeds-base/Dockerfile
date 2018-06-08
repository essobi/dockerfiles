FROM ubuntu:14.04  
MAINTAINER Tomás Godoi <tomas.godoi@stf.jus.br>  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:libreoffice/libreoffice-5-1 && \  
apt-get update && \  
apt-get -y -q install libreoffice=1:5.1\\* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d && \  
echo "deb http://download.mono-project.com/repo/debian wheezy/snapshots/3.12.0
main" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://archive.ubuntu.com/ubuntu precise main universe multiverse"
>> /etc/apt/sources.list && \  
DEBIAN_FRONTEND=noninteractive && \  
locale-gen en_US.UTF-8 && \  
apt-get -y update && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections && \  
apt-get install --force-yes -yq software-properties-common && \  
add-apt-repository ppa:ubuntu-toolchain-r/test && \  
apt-get -y update && \  
apt-get \--force-yes -yq install gcc-4.9 nano htop && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get -y update && apt-get \--force-yes -yq install libc6 libcurl3
libgcc1 libstdc++6 debconf adduser mysql-server-5.6 \  
mono-runtime mono-fastcgi-server nginx nodejs libxml2 supervisor python3
python3-uno libreoffice-writer libreoffice-calc libreoffice-impress \  
fonts-dejavu fonts-liberation ttf-mscorefonts-installer fonts-crosextra-
carlito fonts-takao-gothic libfcgi timelimit && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]

