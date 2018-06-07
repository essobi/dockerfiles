#  
# THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#  
FROM guusk/docker-texlive:2016  
MAINTAINER Guus Kuiper <guuskuiper@gmail.com>  
  
RUN apt-get update -q && apt-get install -qy --no-install-recommends \  
wget gawk bc \  
gnuplot \  
build-essential \  
git \  
poppler-utils \  
imagemagick \  
unzip \  
xzdec \  
ghostscript \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "Europe/Amsterdam" > /etc/timezone && dpkg-reconfigure -f
noninteractive tzdata  
  
RUN tlmgr update --self && tlmgr install siunitx algorithm2e  

