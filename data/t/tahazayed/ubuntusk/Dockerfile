FROM solita/ubuntu-systemd-ssh:latest  
  
  
  
RUN useradd -c "pi the Brave" -m -s /bin/bash pi -d /home/pi && echo
pi:raspberry | chpasswd && usermod -aG sudo pi  
COPY files/SKDownloader /home/pi/github/SKDownloader  
  
RUN sed -i "s/# deb-src/deb-src/g" /etc/apt/sources.list \  
&& apt-get update && apt-get install -y --no-install-recommends apt-utils \  
&& apt-get install -y --no-install-recommends \  
build-essential ca-certificates findutils gnupg dirmngr inetutils-ping \  
iproute netbase curl gcc g++ libcurl4-openssl-dev dh-make devscripts build-
essential \  
fakeroot libspdlog-dev git nano quilt dh-systemd \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR "/home/pi/github/SKDownloader"  
  
RUN . ./build.sh  
  
WORKDIR "/home/pi/github/SKDownloader/build"  
  
RUN dpkg -i skdownloader_*_all.deb  
RUN rm -rf /home/pi/github \  
&& chmod +777 -R /home/pi \  
&& chown pi:pi -R /home/pi \  
&& apt-get remove -y dh-make \  
dh-systemd \  
quilt \  
devscripts \  
build-essential \  
\--allow-remove-essential \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

