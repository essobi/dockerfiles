FROM debian:stretch  
#install mono  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV XDG_CONFIG_HOME="/config"  
RUN apt-get update && apt-get install --no-install-recommends -y gnupg dirmngr
\  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& apt-get update && apt-get install --no-install-recommends -y \  
gosu \  
curl \  
libcurl4-openssl-dev \  
mono-devel \  
ca-certificates-mono \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install latest jackett release  
RUN cd /opt \  
&& version=`curl --silent
"https://api.github.com/repos/Jackett/Jackett/releases/latest" | sed -nr
's/.*"tag_name": "(.*)",/\1/p'` \  
&& echo "install jackett version : ${version}" \  
&& echo " from url : " \  
&& curl -fSL
https://github.com/Jackett/Jackett/releases/download/${version}/Jackett.Binaries.Mono.tar.gz
| tar xz --no-same-owner  
  
COPY . /  
EXPOSE 9117  
VOLUME /config  
ENTRYPOINT ["/entrypoint.sh"]  

