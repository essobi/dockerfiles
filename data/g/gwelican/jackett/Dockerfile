FROM ubuntu:16.04  
LABEL MAINTAINER gwelican <superfly@gwelican.eu>  
  
ENV jackett_version="0.7.1483"  
  
RUN apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/ubuntu xenial main" | tee
/etc/apt/sources.list.d/mono-official.list && \  
apt-get update -qq && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qqy curl bzip2 sudo
libcurl4-openssl-dev mono-devel && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
curl -Lo /tmp/jackett.tar.gz
https://github.com/Jackett/Jackett/releases/download/v${jackett_version}/Jackett.Binaries.Mono.tar.gz
&& \  
mkdir /jackett && \  
tar -xzf /tmp/jackett.tar.gz \--strip-components=1 -C /jackett && \  
rm -f /tmp/jackett.tar.gz && \  
groupadd -o -g 100 jackett && \  
useradd -o -u 1000 -N -g jackett \--shell /bin/sh -d /config jackett && \  
install -o jackett -g jackett -d /config /media && \  
chown jackett:jackett /jackett /config  
# Default container settings  
VOLUME /config  
EXPOSE 9117  
  
WORKDIR "/config"  
  
  
ENTRYPOINT ["/usr/bin/mono", "--debug", "/jackett/JackettConsole.exe"]  
CMD ["-x", "true"]  

