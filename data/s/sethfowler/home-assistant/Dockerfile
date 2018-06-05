# Notice:  
# When updating this file, please also update
virtualization/Docker/Dockerfile.dev  
# This way, the development image and the production image are kept in sync.  
  
FROM python:3.6  
LABEL maintainer="Paulus Schoutsen <Paulus@PaulusSchoutsen.nl>"  
# Uncomment any of the following lines to disable the installation.  
#ENV INSTALL_TELLSTICK no  
#ENV INSTALL_OPENALPR no  
#ENV INSTALL_FFMPEG no  
#ENV INSTALL_LIBCEC no  
#ENV INSTALL_PHANTOMJS no  
#ENV INSTALL_SSOCR no  
##################################################  
# (Added to upstream Dockerfile.)  
##################################################  
# Set environment variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Install dependencies and tools. (This is from marcoraddatz/homebridge-
docker.)  
RUN apt-get update; \  
apt-get install -y apt-utils apt-transport-https; \  
apt-get install -y curl wget; \  
apt-get install -y libnss-mdns avahi-discover libavahi-compat-libdnssd-dev
libkrb5-dev; \  
apt-get install -y ffmpeg; \  
apt-get install -y nano vim  
  
# Install node.  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -; \  
apt-get install -y build-essential nodejs  
  
# Install latest Homebridge  
# -------------------------------------------------------------------------  
# You can force a specific version by setting HOMEBRIDGE_VERSION  
# See https://github.com/marcoraddatz/homebridge-docker#homebridge_version  
# -------------------------------------------------------------------------  
RUN npm install -g homebridge --unsafe-perm  
  
##################################################  
# (End of added stuff.)  
##################################################  
  
VOLUME /config  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Copy build scripts  
COPY virtualization/Docker/ virtualization/Docker/  
RUN virtualization/Docker/setup_docker_prereqs  
  
# Install hass component dependencies  
COPY requirements_all.txt requirements_all.txt  
# Uninstall enum34 because some dependencies install it but breaks Python
3.4+.  
# See PR #8103 for more info.  
RUN pip3 install --no-cache-dir -r requirements_all.txt && \  
pip3 install --no-cache-dir mysqlclient psycopg2 uvloop cchardet cython  
  
# Copy source  
COPY . .  
  
##################################################  
# (Added to upstream Dockerfile.)  
##################################################  
# MISC settings. This is all configuration for homebridge.  
COPY docker-scripts/avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
  
USER root  
RUN mkdir -p /var/run/dbus  
  
# This would be needed for homebridge, but hass requires `--net=host` anyway.  
# EXPOSE 5353 51826  
  
RUN apt-get update && \  
apt-get install -y git  
  
# Upstream uses the command below, but I've added a wrapper that does
additional  
# runtime configuration and starts homebridge.  
# CMD [ "python", "-m", "homeassistant", "--config", "/config" ]  
CMD ["./docker-scripts/run.sh"]  
  
##################################################  
# (End of added stuff.)  
##################################################  

