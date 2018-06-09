FROM alpine:3.7  
MAINTAINER Chris Kankiewicz <Chris@ChrisKankiewicz.com>  
  
# Define Syncthing version  
ARG ST_VERSION=0.14.48  
# Set some environment variables  
ENV STNODEFAULTFOLDER true  
ENV STNOUPGRADE true  
  
# Create Syncthing directories  
RUN mkdir -p /etc/syncthing /opt/syncthing /vol/storage  
  
# Create non-root user  
RUN adduser -DHs /sbin/nologin syncthing  
  
# Set tarball file URL  
ARG
TARBALL_URL=https://github.com/syncthing/syncthing/releases/download/v${ST_VERSION}/syncthing-
linux-386-v${ST_VERSION}.tar.gz  
  
# Install dependencies  
RUN apk add --update ca-certificates tar tzdata wget \  
&& wget -qO- ${TARBALL_URL} | tar -xz --strip-components=1 -C /opt/syncthing \  
&& apk del ca-certificates tar wget && rm -rf /var/cache/apk/* \  
&& chown -R syncthing:syncthing /etc/syncthing /opt/syncthing /vol/storage  
  
# Create symlink to binary in the $PATH  
RUN ln -s /opt/syncthing/syncthing /usr/local/bin/syncthing  
  
# Expose ports  
EXPOSE 8384 22000 21027/udp  
  
# Set running user  
USER syncthing  
  
# Create volumes  
VOLUME /etc/syncthing /vol/storage  
  
# Set the working dir  
WORKDIR /opt/syncthing  
  
# Set command  
CMD ["syncthing", "-gui-address=0.0.0.0:8384", "-home=/etc/syncthing", "-no-
browser"]  

