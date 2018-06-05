FROM node  
MAINTAINER Markus Kosmal <code@m-ko-x.de>  
  
RUN apt-get update -yqq && DEBIAN_FRONTEND=noninteractive apt-get install -yqq
--no-install-recommends \  
libasound2 \  
libgconf-2-4 \  
libgnome-keyring-dev \  
libgnome-keyring-dev \  
libgtk2.0-0 \  
libnss3 \  
libxtst6 && \  
apt-get clean -yqq && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /src  
  
RUN LATEST_TAG=`git ls-remote --tags https://github.com/atom/atom | sort -t
'/' -k3 --version-sort | tail -n1 | cut -d'/' -f3` && \  
git clone -b $LATEST_TAG https://github.com/atom/atom --depth 1 /src && \  
script/build && script/grunt install && \  
rm -fr /src  
  
# Startup  
CMD /usr/local/bin/atom --foreground --log-file /var/log/atom.log && tail -f
/var/log/atom.log  

