FROM alpine:3.6  
MAINTAINER Pierre GINDRAUD <pgindraud@gmail.com>  
  
ARG OVERLAY_VERSION=v1.18.1.5  
ARG OVERLAY_ARCH=amd64  
  
ENV SMTP_PORT=25 \  
SMTP_STARTTLS=no \  
SMTP_SSL=no  
#SMTP_USERNAME=SASL_USERNAME \  
#SMTP_PASSWORD=SASL_PASSWORD \  
#SMTP_SERVER=  
# Install dependencies  
RUN apk --no-cache add \  
curl \  
jq \  
ssmtp \  
transmission-daemon && \  
# install s6 overlay  
curl -L -s "https://github.com/just-
containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz"
\  
| tar xvzf - -C / && \  
# purge install  
apk del --no-cache curl  
  
# copy local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 9091/tcp 51413  
VOLUME ["/config","/downloads","/watch"]  
WORKDIR /downloads  
  
ENTRYPOINT [ "/init" ]  

