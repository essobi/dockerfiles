FROM arizonaa/baseimage-xenial  
MAINTAINER sparklyballs  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# environment settings  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV XDG_DATA_HOME="/config" \  
XDG_CONFIG_HOME="/config"  
  
# adding mono repo  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" \  
| tee /etc/apt/sources.list.d/mono-xamarin.list && \  
  
# install packages  
apt-get update && \  
apt-get install -y \  
bzip2 \  
curl \  
libcurl4-openssl-dev \  
mono-devel \  
wget && \  
  
# install Jackett  
mkdir -p \  
/app/Jackett && \  
jack_tag=$(curl -sX GET
"https://api.github.com/repos/Jackett/Jackett/releases/latest" \  
| awk '/tag_name/{print $4;exit}' FS='[""]') && \  
curl -o \  
/tmp/jacket.tar.gz -L \  
https://github.com/Jackett/Jackett/releases/download/$jack_tag/Jackett.Binaries.Mono.tar.gz
&& \  
tar xf \  
/tmp/jacket.tar.gz -C \  
/app/Jackett \--strip-components=1 && \  
  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /downloads  
EXPOSE 9117  

