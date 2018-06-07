FROM alpine:3.6  
ENV appdir /app  
ENV PKGVER=0.16.0  
ENV
PKGSOURCE=https://github.com/fatedier/frp/releases/download/v${PKGVER}/frp_${PKGVER}_linux_amd64.tar.gz  
  
RUN mkdir -p $appdir  
WORKDIR $appdir  
  
RUN apk add --no-cache --update wget \  
&& wget $PKGSOURCE \--no-check-certificate \  
&& tar -zxf frp_${PKGVER}_linux_amd64.tar.gz \  
&& mv frp_${PKGVER}_linux_amd64 frp \  
&& rm frp_${PKGVER}_linux_amd64.tar.gz \  
&& apk del wget  
  
WORKDIR $appdir/frp  
  
EXPOSE 80 443 6000 7000 7500  

