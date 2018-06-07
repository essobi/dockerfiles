FROM alpine:latest  
MAINTAINER Andreas Wölfl andreas.woelfl84@gmail.com  
  
# environment variables  
ENV PLATFORM_ARCH="amd64"  
ENV ENCFS6_CONFIG="/config/encfs.xml"  
# install packages  
RUN apk add --no-cache curl tar wget encfs  
  
# install s6 overlay  
RUN \  
OVERLAY_VERSION=$(curl -sX GET "https://api.github.com/repos/just-
containers/s6-overlay/releases/latest" | awk '/tag_name/{print $4;exit}'
FS='[""]') && \  
curl -o /tmp/s6-overlay.tar.gz -L "https://github.com/just-
containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${PLATFORM_ARCH}.tar.gz"
&& \  
tar xfz /tmp/s6-overlay.tar.gz -C /  
  
# remove packages  
RUN apk del curl tar wget  
  
# create dirs  
RUN mkdir -p /encrypted /decrypted /config  
  
# copy services  
COPY root/ /  
  
# create volumes  
VOLUME /encrypted /decrypted /config  
  
ENTRYPOINT ["/init"]  

