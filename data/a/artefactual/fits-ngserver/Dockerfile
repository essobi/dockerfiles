FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ARG FITS_VERSION=0.8.4-1~14.04  
ARG FITS_USER=fits  
ARG FITS_UID=333  
ARG FITS_GROUP=fits  
ARG FITS_GID=333  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-transport-https \  
curl \  
python-software-properties \  
software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -ex \  
&& curl -s https://packages.archivematica.org/GPG-KEY-archivematica | apt-key
add - \  
&& add-apt-repository "deb [arch=amd64]
http://packages.archivematica.org/1.6.x/ubuntu-externals trusty main" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
fits=$FITS_VERSION \  
nailgun \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -ex \  
&& groupadd --system --gid ${FITS_GID} ${FITS_GROUP} \  
&& useradd --system --uid ${FITS_UID} \--gid ${FITS_GID} ${FITS_USER}  
  
USER fits  
EXPOSE 2113  
ENTRYPOINT ["/usr/bin/fits-ngserver.sh", "/usr/share/maven-
repo/com/martiansoftware/nailgun-server/debian/nailgun-server-debian.jar"]  

