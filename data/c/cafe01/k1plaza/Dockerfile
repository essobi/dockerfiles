FROM debian:9-slim AS base  
  
COPY ./cpanfile /root  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y wget lsb-release gnupg libterm-readline-gnu-perl && \  
wget https://dev.mysql.com/get/mysql-apt-config_0.8.9-1_all.deb -O
/root/mysql-apt.config.deb && \  
dpkg -i /root/mysql-apt.config.deb && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
wget \  
ca-certificates \  
build-essential \  
uuid-dev \  
libgmp3-dev \  
libxml2-dev \  
libexpat1-dev \  
zlib1g-dev \  
libssl-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
libgif-dev \  
libv8-dev \  
libmysqlclient-dev \  
libssh2-1-dev && \  
wget -O- http://git.io/cpm | perl - install --global --cpanfile=/root/cpanfile
&& \  
rm -rf /root/.perl-cpm/* /root/.cpanm/* /usr/local/share/man/* /root/*.deb &&
\  
apt-get remove build-essential -y && \  
apt-get autoremove -y && \  
apt-get clean -y  
  
RUN useradd -ms /bin/bash k1plaza  
WORKDIR /k1plaza  
RUN mkdir file_storage repositories managed_apps && \  
chown k1plaza:k1plaza file_storage repositories managed_apps  
  
RUN apt-get install -y --no-install-recommends sudo && \  
apt-get clean -y && \  
echo 'k1plaza ALL=(ALL:ALL) NOPASSWD: ALL' > /etc/sudoers.d/k1plaza  
  
EXPOSE 3000  
STOPSIGNAL QUIT  
USER k1plaza:k1plaza  
  
  
  
FROM base AS production  
ADD ./share share  
ADD ./script script  
ADD ./lib lib  
ENV MOJO_MODE production  
ENTRYPOINT ["hypnotoad", "./script/k1plaza", "-f"]  
  
FROM production AS developer  
USER root  
RUN mkdir -p /usr/share/man/man1/ && \  
apt-get install -y --no-install-recommends openjdk-8-jdk-headless && \  
apt-get clean -y  
  
USER k1plaza  
ENV K1PLAZA_DEVELOPER=1 MOJO_MODE=development  
STOPSIGNAL TERM  
ENTRYPOINT ["./script/k1plaza", "daemon"]  

