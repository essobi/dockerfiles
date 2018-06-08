FROM sdhibit/alpine-runit:3.6  
MAINTAINER Steve Hibit <sdhibit@gmail.com>  
  
RUN addgroup -S madsonic \  
&& adduser -SHG madsonic madsonic  
  
# Install apk packages  
RUN apk --update upgrade \  
&& apk --no-cache add \  
openjdk8-jre-base \  
unzip \  
wget  
  
# Set Madsonic Package Information  
ENV PKG_NAME madsonic  
ENV PKG_VER 6.2.9080  
ENV PKG_VERA 6.2  
ENV PKG_DATE 20161222  
ENV APP_BASEURL http://www.madsonic.org/download  
ENV APP_PKGNAME ${PKG_DATE}_${PKG_NAME}-${PKG_VER}-standalone.zip  
ENV TRAN_PKGNAME ${PKG_DATE}_${PKG_NAME}-transcode-linux-x64.zip  
ENV APP_URL ${APP_BASEURL}/${PKG_VERA}/${APP_PKGNAME}  
ENV TRAN_URL ${APP_BASEURL}/transcode/${TRAN_PKGNAME}  
ENV APP_PATH /var/madsonic  
  
# Download & Install Madsonic  
RUN mkdir -p "${APP_PATH}/transcode" \  
&& wget -O "${APP_PATH}/madsonic.zip" ${APP_URL} \  
&& wget -O "${APP_PATH}/transcode/transcode.zip" ${TRAN_URL} \  
&& unzip "${APP_PATH}/madsonic.zip" -d ${APP_PATH} \  
&& unzip "${APP_PATH}/transcode/transcode.zip" -d "${APP_PATH}/transcode" \  
&& rm "${APP_PATH}/madsonic.zip" \  
&& rm "${APP_PATH}/transcode/transcode.zip"  
# Change ownership  
RUN mkdir /config \  
&& chown -R madsonic:madsonic \  
${APP_PATH} \  
"/config"  
  
VOLUME ["/config"]  
  
# HTTP ports  
EXPOSE 4040  
EXPOSE 4050  
WORKDIR /var/madsonic  
  
# Add services to runit  
ADD madsonic.sh /etc/service/madsonic/run  
RUN chmod +x /etc/service/*/run  

