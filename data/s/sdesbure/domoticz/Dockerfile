FROM debian:stretch  
MAINTAINER Sylvain Desbureaux <sylvain@desbureaux.fr>  
  
# install packages &  
## OpenZwave installation &  
# grep git version of openzwave &  
# untar the files &  
# compile &  
# "install" in order to be found by domoticz &  
## Domoticz installation &  
# clone git source in src &  
# Domoticz needs the full history to be able to calculate the version string &  
# prepare makefile &  
# compile &  
# remove git and tmp dirs  
  
RUN apt-get update && apt-get install -y --no-install-recommends --fix-missing
\  
git \  
libssl1.0.2 libssl-dev \  
build-essential cmake \  
libboost-dev \  
libboost-thread1.62.0 libboost-thread-dev \  
libboost-system1.62.0 libboost-system-dev \  
libboost-date-time1.62.0 libboost-date-time-dev \  
libsqlite3-0 libsqlite3-dev \  
curl libcurl3 libcurl4-openssl-dev \  
libusb-0.1-4 libusb-dev \  
zlib1g-dev \  
libudev-dev \  
linux-headers-amd64 \  
python3-dev \  
ca-certificates && \  
git clone --depth 2 https://github.com/OpenZWave/open-zwave.git /src/open-
zwave && \  
cd /src/open-zwave && \  
make && \  
ln -s /src/open-zwave /src/open-zwave-read-only && \  
git clone --depth 2 https://github.com/domoticz/domoticz.git /src/domoticz &&
\  
cd /src/domoticz && \  
git fetch --unshallow && \  
cmake -DCMAKE_BUILD_TYPE=Release . && \  
make && \  
apt-get remove -y git cmake linux-headers-amd64 build-essential libssl-dev
libboost-dev libboost-thread-dev libboost-system-dev libsqlite3-dev
libcurl4-openssl-dev libusb-dev zlib1g-dev libudev-dev python3-dev && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /src/domoticz/.git && \  
rm -rf /src/open-zwave/.git  
  
ARG VCS_REF  
ARG BUILD_DATE  
  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/domoticz/domoticz" \  
org.label-schema.url="https://domoticz.com/" \  
org.label-schema.name="Domoticz" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="GPLv3" \  
org.label-schema.build-date=$BUILD_DATE  
  
  
VOLUME /config  
  
EXPOSE 8080  
  
HEALTHCHECK --interval=5m \--timeout=3s \  
CMD curl -f http://localhost:8080/ || exit 1  
  
ENTRYPOINT ["/src/domoticz/domoticz", "-dbase", "/config/domoticz.db"]  
CMD ["-www", "8080"]  

