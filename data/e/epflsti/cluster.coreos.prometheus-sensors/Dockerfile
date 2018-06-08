# Merge sensor-exporter (https://github.com/amkay/sensor-exporter)  
# with hddtemp (https://github.com/Drewster727/hddtemp-docker)  
# docker build -t epflsti/cluster.coreos.prometheus-sensors .  
# docker run -i -t epflsti/cluster.coreos.prometheus-sensors bash  
# @TODO: find which capabilities' needed instead of privilegied (note:
sys_admin cap not working)  
# docker run --privileged=true -v "/dev":"/dev":rw --publish=9192:9255
--name=cluster.coreos.prometheus-sensors epflsti/cluster.coreos.prometheus-
sensors  
# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:latest  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Install hddtemp  
RUN apt-get update && apt-get -y install \  
build-essential \  
gcc \  
libc-dev \  
hddtemp \  
lm-sensors \  
libsensors4-dev \  
git \  
golang-go  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /go  
ENV GOPATH=/go  
  
RUN go get \  
github.com/amkay/gosensors \  
github.com/prometheus/client_golang/prometheus  
  
# Copy the local package files to the container's workspace.  
ADD sensor-exporter /go/src/github.com/ncabatoff/sensor-exporter  
  
RUN go install github.com/ncabatoff/sensor-exporter  
  
# Run the outyet command by default when the container starts.  
ENTRYPOINT [ "/bin/bash", "-c", "set -x; hddtemp -q -d -F /dev/sd? &
/go/bin/sensor-exporter" ]  
  
# Document that the service listens on port 9255.  
EXPOSE 9255  

