# Download base image  
FROM barbak/debian-s6:latest  
  
# Define the ARG variables for creating docker image  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
ARG
PACKAGE_VERSION_URL=http://www.mysqueezebox.com/update/?version=7.9.1&revision=1&geturl=1&os=deb  
  
# Labels  
LABEL org.label-schema.name="LogitechMediaServer" \  
org.label-schema.description="Logitech Media Server Docker image" \  
org.label-schema.vendor="Paul NOBECOURT <paul.nobecourt@orange.fr>" \  
org.label-schema.url="https://github.com/pnobecourt/" \  
org.label-schema.version=$VERSION \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/pnobecourt/docker-
logitechmediaserver" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0"  
  
# Define the ENV variable for creating docker image  
ENV LANG=C.UTF-8 \  
DEBIAN_FRONTEND=noninteractive \  
SHELL=/bin/bash \  
TERM=xterm \  
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \  
PS1=$(whoami)@$(hostname):$(pwd)$ \  
SQUEEZE_VOL=/srv/apps/squeezebox  
  
# LogitechMediaServer installation  
RUN echo "deb http://www.deb-multimedia.org stretch main non-free" | tee -a
/etc/apt/sources.list.d/debian-multimedia.list && \  
apt-get update ; \  
apt-get install -y --allow-unauthenticated --no-install-recommends deb-
multimedia-keyring && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
faac \  
faad \  
ffmpeg \  
flac \  
lame \  
libcrypt-openssl-rsa-perl \  
libio-socket-inet6-perl \  
libio-socket-ssl-perl \  
libmoosex-role-timer-perl \  
libwww-perl \  
locales \  
perl \  
perl-base \  
sox \  
wavpack \  
wget \  
&& \  
url=$(curl "$PACKAGE_VERSION_URL" | sed 's/_all\.deb/_amd64\.deb/') && \  
curl -Lsf -o /tmp/logitechmediaserver.deb $url && \  
dpkg -i /tmp/logitechmediaserver.deb && \  
apt-get install -f -y --no-install-recommends && \  
apt-get purge -y curl && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/log/* \  
/var/tmp/* \  
&& \  
userdel squeezeboxserver  
  
# Add files  
ADD /root /  
  
# Ports configuration  
EXPOSE 3483 3483/udp 5353 5353/udp 9000 9005 9010 9090  
  
# Entrypoint  
ENTRYPOINT [ "/init" ]  

