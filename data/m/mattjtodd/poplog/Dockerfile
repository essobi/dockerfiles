FROM debian:jessie-slim  
  
WORKDIR /usr/local/poplog  
  
ARG POPLOG_VERSION=v15.65  
  
ENV POPLOG_INSTALLER=get-and-install-prelinked-$POPLOG_VERSION-poplog  
  
RUN set -ex && \  
sed -i '/:main*$/ ! s/$/ contrib/' /etc/apt/sources.list && \  
dpkg --add-architecture i386 && \  
apt-get update && apt-get upgrade -y && \  
apt-get install -y \  
wget \  
libblas-dev:i386 \  
liblapack-dev:i386 \  
libc6:i386 \  
libncurses5:i386 \  
libstdc++6:i386 \  
gcc \  
build-essential \  
tcsh \  
libxext6:i386 \  
libxext-dev:i386 \  
libx11-6:i386 \  
libx11-dev:i386 \  
libxt-dev:i386 \  
libmotif-dev:i386 \  
libncurses5-dev:i386 \  
espeak \  
xterm && \  
wget http://www.cs.bham.ac.uk/research/projects/poplog/latest-
poplog/$POPLOG_INSTALLER && \  
sh $POPLOG_INSTALLER  
  
ENTRYPOINT ["./poplog.sh", "basepop11"]  

