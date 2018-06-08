########################################################################################################  
# Murmur (Mumble) server runner.  
# Volume mount points:  
# /Data - murmur database and ini files. (Better to hold in volume container
or host).  
# Variables:  
# MURMUR_VERSION - murmur version to download and run.  
########################################################################################################  
#FROM debian:jessie  
FROM ubuntu:14.04  
# wget to download murmur  
RUN apt-get update && apt-get install -y wget bzip2  
  
# User ID and group ID to set volume owner (Default 2000).  
ENV UID 2000  
ENV GID 2000  
  
# USER "runner" with uid "2000" to run server.  
RUN groupadd -g $GID runner && useradd -g runner runner -u $UID  
  
ENV MURMUR_VERSION=1.2.12  
  
# Server location.  
RUN mkdir /Server && chown $UID:$GID /Server  
# Data location.  
RUN mkdir /Data && chown $UID:$GID /Data  
  
# Run as user.  
USER runner  
WORKDIR /Server  
  
# Download and extract murmur.  
RUN wget https://github.com/mumble-
voip/mumble/releases/download/${MURMUR_VERSION}/murmur-
static_x86-${MURMUR_VERSION}.tar.bz2 && \  
bzcat ./murmur-static_x86-${MURMUR_VERSION}.tar.bz2 | tar -x -f - && \  
rm ./murmur-static_x86-${MURMUR_VERSION}.tar.bz2 && \  
mv ./murmur-static_x86-${MURMUR_VERSION}/* ./ && rm -R ./murmur-
static_x86-${MURMUR_VERSION}/  
  
# Create default murmur.ini  
RUN cat murmur.ini | \  
sed 's/^database=/database=\/Data\/murmur.sqlite/' | \  
sed 's/^#logfile=murmur.log/logfile=\/Data\/murmur.log/' | \  
sed 's/^#host=/host=0.0.0.0/'> /Data/murmur.ini  
  
  
# Ports for murmur.  
EXPOSE 64738 64738/udp  
  
# Volume for murmur.ini and server database.  
VOLUME ["/Data"]  
  
# Run as root, then swithc to uname user in murmur.ini  
  
# Run murmur  
ENTRYPOINT ["./murmur.x86", "-fg", "-v"]  
CMD ["-ini", "/Data/murmur.ini"]  

