FROM debian:jessie  
MAINTAINER DracoDragon88  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get install -y apt-utils git-core xz-utils curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
RUN apt install apt-transport-https \  
RUN echo "deb https://download.mono-project.com/repo/debian stable-jessie
main" | tee /etc/apt/sources.list.d/mono-official-stable.list \  
RUN apt update  
  
# Common  
ENV FX_VERSION 638-c36234473789b1af366b5fdc80a07f87c2755ddb  
ENV FX_DOWNLOAD_URL
https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/$FX_VERSION/fx.tar.xz  
ENV FX_RESOURCES_URL https://github.com/citizenfx/cfx-server-data.git  
ENV FX_PATH "/fivem/fx-server"  
ENV FX_PATH_DATA "/fivem/fx-server-data"  
ENV FX_ARCHIVE fx.tar.xz  
ENV FX_PORT 30120  
# Container Setup  
RUN mkdir /fivem && \  
mkdir "$FX_PATH" && \  
mkdir "$FX_PATH_DATA" && \  
mkdir /opt/cfx-server && \  
cd /fivem && \  
curl -fsSL "$FX_DOWNLOAD_URL" -o "$FX_ARCHIVE" && \  
git clone "$FX_RESOURCES_URL" "$FX_PATH_DATA" && \  
tar -xvf "$FX_ARCHIVE" -C "$FX_PATH" && \  
rm "$FX_ARCHIVE"  
  
RUN chmod -R 775 "$FX_PATH"  
RUN chmod -R 775 "$FX_PATH_DATA"  
  
COPY server.cfg /"$FX_PATH_DATA"/server.cfg  
  
WORKDIR "$FX_PATH_DATA"  
  
EXPOSE "$FX_PORT"  
EXPOSE "$FX_PORT"/udp  
  
CMD "$FX_PATH"/run.sh +exec server.cfg  

