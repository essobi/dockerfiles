FROM golang:alpine  
  
RUN apk add --no-cache curl bash git ca-certificates wget \  
&& update-ca-certificates \  
&& curl -sSO https://raw.githubusercontent.com/pote/gpm/v1.4.0/bin/gpm \  
&& chmod +x gpm \  
&& mv gpm /usr/local/bin  
  
ENV BURROW_EXPORTER_VERSION v0.0.2  
RUN wget
https://github.com/jirwin/burrow_exporter/releases/download/$BURROW_EXPORTER_VERSION/burrow-
exporter_linux_amd64.zip \  
&& unzip burrow-exporter_linux_amd64.zip \  
&& rm burrow-exporter_linux_amd64.zip  
  
ENV BURROW_URL ""  
ENV METRICS_PORT 9999  
ENV METRICS_INTERVAL 60  
CMD ./dist/linux_amd64/burrow-exporter --burrow-addr "${BURROW_URL}"
\--metrics-addr 0.0.0.0:"${METRICS_PORT}" \--interval "${METRICS_INTERVAL}"  

