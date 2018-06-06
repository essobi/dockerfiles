FROM debian:sid  
LABEL maintainer "Krystan Honour <krystan@gmail.com>"  
  
# docker run -it \  
# --net host \  
# --cpuset-cpus 0 \  
# --memory 1500mb \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# -e GOPATH=/projects/project1  
# --security-opt seccomp=$HOME/goland.json \  
# --device /dev/snd \  
# --device /dev/dri \  
# -v /dev/shm:/dev/shm \  
# -v $HOME/.golandhome:/home/goland \  
# --name goland \  
# --rm \  
# krystan/goland  
# Install goland  
WORKDIR /opt/goland  
  
ARG GOLANDVERSION=goland-2018.1.2  
ARG GOLANGVERSION=1.10.2  
ENV GOROOT=/usr/local/go  
ENV GOPATH=/home/goland/GolandProjects  
ENV DISPLAY=unix$DISPLAY  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
git-core \  
libsecret-1-0 gnome-keyring \  
gnupg \  
hicolor-icon-theme \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpango1.0-0 \  
libpulse0 \  
libv4l-0 \  
fonts-symbola \  
\--no-install-recommends  
  
RUN curl -sSL -O https://download.jetbrains.com/go/${GOLANDVERSION}.tar.gz \  
&& mkdir goland \  
&& tar -xzvf ${GOLANDVERSION}.tar.gz -C ./goland/ \  
\--strip-components=1 \  
&& curl -sSL -O
https://storage.googleapis.com/golang/go${GOLANGVERSION}.linux-amd64.tar.gz \  
&& tar -xzvf go${GOLANGVERSION}.linux-amd64.tar.gz \  
&& mv go /usr/local \  
&& rm *.tar.gz \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
RUN groupadd -g 999 goland \  
&& useradd -r -u 999 -g goland -G audio,video goland \  
&& mkdir -p /home/goland \  
&& chown -R goland:goland /home/goland \  
&& chown -R goland:goland /opt/goland \  
&& export PATH=$GOPATH/bin:$GOROOT/bin:$PATH  
  
# Run GoLand as non privileged user  
USER goland  
  
# Autorun GoLand  
CMD [ "./goland/bin/goland.sh" ]  

