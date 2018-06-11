FROM alpine:latest  
MAINTAINER Andreas Wölfl andreas.woelfl84@gmail.com  
  
# environment variables  
ENV PLATFORM_ARCH="amd64"  
# install packages  
RUN apk add --no-cache curl tar wget unionfs-fuse  
  
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
RUN mkdir -p /source1 /source2 /target  
  
# copy services  
COPY root/ /  
  
# create volumes  
VOLUME /source1 /source2 /target  
  
ENTRYPOINT ["/init"]  

