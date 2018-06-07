FROM sdhibit/mono:5.4  
MAINTAINER Steve Hibit <sdhibit@gmail.com>  
  
# Install apk packages  
RUN apk --update upgrade \  
&& apk --no-cache add \  
bzip2 \  
ca-certificates \  
libcurl \  
openssl \  
sqlite \  
sqlite-libs \  
tar \  
unrar \  
&& update-ca-certificates \  
&& cert-sync /etc/ssl/certs/ca-certificates.crt  
  
# Set Jackett Package Information  
ENV PKG_NAME Jackett  
ENV PKG_VER 0.7  
ENV PKG_BUILD 1523  
ENV APP_BASEURL https://github.com/Jackett/Jackett/releases/download  
ENV APP_PKGNAME v${PKG_VER}.${PKG_BUILD}/${PKG_NAME}.Binaries.Mono.tar.gz  
ENV APP_URL ${APP_BASEURL}/${APP_PKGNAME}  
ENV APP_PATH /opt/jackett  
  
# Mono Environment settings  
ENV XDG_DATA_HOME /config  
ENV XDG_CONFIG_HOME /config  
  
# Download & Install Sonarr  
RUN mkdir -p ${APP_PATH} \  
&& curl -kL ${APP_URL} | tar -xz -C ${APP_PATH} \--strip-components=1  
  
# Create user and change ownership  
RUN mkdir /config \  
&& addgroup -g 666 -S jackett \  
&& adduser -u 666 -SHG jackett jackett \  
&& chown -R jackett:jackett \  
${APP_PATH} \  
"/config" \  
&& ln -s /config /usr/share/Jackett  
  
VOLUME ["/config"]  
  
# Default Jackett server ports  
EXPOSE 9117  
WORKDIR ${APP_PATH}  
  
# Add services to runit  
ADD jackett.sh /etc/service/jackett/run  
RUN chmod +x /etc/service/*/run  

