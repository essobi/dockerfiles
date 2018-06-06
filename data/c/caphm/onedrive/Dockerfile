FROM debian as builder  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV TERM="xterm" LANG="C.UTF-8" LC_ALL="C.UTF-8"  
RUN apt-get update && apt-get -y install libcurl4-openssl-dev libsqlite3-dev
wget gcc unzip make git  
  
WORKDIR /tmp/build/su-exec  
RUN git clone https://github.com/ncopa/su-exec source && cd source && make  
  
WORKDIR /tmp/build/onedrive  
RUN wget
http://downloads.dlang.org/releases/2.x/2.075.1/dmd_2.075.1-0_amd64.deb -O
dmd.deb && dpkg -i dmd.deb \  
&& git clone https://github.com/skilion/onedrive source && cd source && make  
  
FROM debian  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV TERM="xterm" LANG="C.UTF-8" LC_ALL="C.UTF-8"  
COPY \--from=builder /tmp/build/su-exec/source/su-exec
/tmp/build/onedrive/source/onedrive /usr/local/bin/  
COPY \--from=builder /tmp/build/onedrive/source/onedrive.service
/usr/lib/systemd/user/  
  
ENV ONEDRIVE_UID=1000 ONEDRIVE_GID=1000  
VOLUME /config /onedrive  
  
# Fetch dependencies, install DMD (D language) which OneDrive Free Client
relies on,  
# install the OneDrive Free Client, then remove some packages to slim down the
image  
# and create user inside the container  
RUN apt-get update \  
&& apt-get -y install libcurl4-openssl-dev libsqlite3-dev \  
&& useradd -U -d /config -s /bin/false onedrive \  
&& usermod -G users onedrive  
  
ADD ./entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/local/bin/onedrive", "-m", "--confdir=/config", "--
syncdir=/onedrive"]  

