FROM alpine:3.7  
MAINTAINER Chris Kankiewicz <Chris@ChrisKankiewicz.com>  
  
# Define PlexPy version  
ARG PLEXPY_VERSION=1.4.25  
# Create PlexPy directories  
RUN mkdir -pv /opt/plexpy /etc/plexpy  
  
# Create non-root user  
RUN adduser -DHs /sbin/nologin plexpy  
  
# Install dependencies  
RUN apk add --update python && rm -rf /var/cache/apk/*  
  
# Set PlexPy archive URL  
ARG
TARBALL_URL=https://api.github.com/repos/drzoidberg33/plexpy/tarball/v${PLEXPY_VERSION}  
  
# Download and extract PlexPy archive  
RUN apk add --update ca-certificates tar tzdata wget \  
&& wget -qO- ${TARBALL_URL} | tar -xzv --strip-components=1 -C /opt/plexpy \  
&& apk del tar wget && rm -rf /var/cache/apk/* \  
&& chown -R plexpy:plexpy /etc/plexpy /opt/plexpy  
  
# Expose ports  
EXPOSE 8181  
# Set running user  
USER plexpy  
  
# Define volumes  
VOLUME /etc/plexpy  
  
# Default command  
CMD ["/opt/plexpy/PlexPy.py", "--nolaunch", "--verbose", "--datadir",
"/etc/plexpy"]  

