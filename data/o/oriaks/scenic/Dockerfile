FROM debian:jessie  
MAINTAINER Michael Richard <mrichard@sat.qc.ca>  
  
RUN apt-get update -q  
  
#  
# libshmdata  
#  
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-
recommends autoconf automake bison build-essential flex git libtool
python3-dev && \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends
libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev  
RUN git -c http.sslVerify=false clone -b develop 'https://github.com/sat-
metalab/shmdata.git' /usr/src/libshmdata  
RUN cd /usr/src/libshmdata && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
ldconfig  
  
#  
# switcher  
#  
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-
recommends autoconf automake bison build-essential flex git libtool python-dev
&& \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends
libcgsi-gsoap-dev libglib2.0-dev libgstreamer1.0-dev libgstreamer-plugins-
base1.0-dev libjson-glib-dev && \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends
libgtk2.0-dev libjack-jackd2-dev liblo-dev libportmidi-dev libpulse-dev
libvncserver-dev linux-libc-dev nodejs-dev && \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends
gstreamer1.0-libav gstreamer1.0-plugins-bad gstreamer1.0-plugins-base
gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly  
RUN git -c http.sslVerify=false clone -b develop 'https://github.com/sat-
metalab/switcher.git' /usr/src/switcher  
RUN sed -i '/^if SWITCHERBUILD/,/^endif/{s|^\\(.*\\)|#\1|}'
/usr/src/switcher/Makefile.am  
RUN cd /usr/src/switcher && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
ldconfig  
  
#  
# scenic2  
#  
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-
recommends build-essential git npm ruby-dev && \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends
nodejs nodejs-legacy python ruby && \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends
gstreamer1.0-libav gstreamer1.0-plugins-bad gstreamer1.0-plugins-base
gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-pulseaudio
gstreamer1.0-x libgtk2.0-0 libjack-jackd2-0 liblo7 libportmidi0 libpulse0
libpulse-mainloop-glib0 libvncserver0 libjson-glib-1.0-0 libpython2.7
pulseaudio  
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-
recommends apt-transport-https lsb-release curl && \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends
sudo && \  
curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
&& \  
echo 'deb https://deb.nodesource.com/node_5.x jessie main' >
/etc/apt/sources.list.d/nodejs.list && \  
apt-get update -q && \  
DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends
nodejs  
RUN git -c http.sslVerify=false clone -b develop 'https://github.com/sat-
metalab/scenic.git' /opt/scenic2  
RUN cd /opt/scenic2 && \  
npm install  
  
#  
# cleanup  
#  
RUN rm -rf /usr/src/libshmdata && \  
rm -rf /usr/src/switcher  
RUN apt-get -y purge autoconf automake bison build-essential flex git libtool
python3-dev && \  
apt-get -y purge libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev && \  
apt-get -y purge autoconf automake bison build-essential flex git libtool
python-dev && \  
apt-get -y purge libcgsi-gsoap-dev libglib2.0-dev libgstreamer1.0-dev
libgstreamer-plugins-base1.0-dev libjson-glib-dev && \  
apt-get -y purge libgtk2.0-dev libjack-jackd2-dev liblo-dev libportmidi-dev
libpulse-dev libvncserver-dev linux-libc-dev nodejs-dev && \  
apt-get -y purge build-essential git npm ruby-dev && \  
apt-get -y --purge autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 5060  
EXPOSE 8000  
EXPOSE 8080  
EXPOSE 9000  
ENV PULSE_SERVER /run/pulse/native  
ENV NODE_PATH $NODE_PATH:/usr/local/lib/nodejs:/usr/lib/nodejs  
WORKDIR /opt/scenic2  
  
ENTRYPOINT ["npm","start"]  

