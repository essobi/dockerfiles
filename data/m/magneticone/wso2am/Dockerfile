FROM openjdk:jre-alpine  
  
LABEL Maintainer="SystemOne Team <admins@systemone.tech>"  
  
ARG APIM_VERSION=${APIM_VERSION:-2.2.0-update4}  
  
RUN apk add --update --no-cache \  
bash openssl unzip wget xmlstarlet \  
&& wget -O /tmp/wso2am.zip https://github.com/wso2/product-
apim/releases/download/v${APIM_VERSION}/wso2am-${APIM_VERSION}.zip \  
&& unzip /tmp/wso2am.zip -d /opt \  
&& mv "/opt/wso2am-${APIM_VERSION}" /opt/wso2am \  
&& rm -rf /tmp/*  
  
COPY scripts/ /usr/local/bin/  
  
EXPOSE 5672 7611 7711 8280 8243 8672 9099 9443 9611 9711 9763 9999  
WORKDIR /opt/wso2am  
  
ENTRYPOINT [ "docker-entrypoint.sh" ]  
  
CMD [ "wso2am" ]

