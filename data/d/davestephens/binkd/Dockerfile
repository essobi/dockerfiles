FROM gliderlabs/alpine:3.4  
MAINTAINER Dave Stephens <dave@force9.org>  
  
# we need to get requirements, clone binkd, compile it and remove the
requirements  
# in one step. we do this to stop each command being saved as a separate
layer,  
# saving ~187mb!  
RUN apk add build-base \  
gcc \  
abuild \  
binutils \  
binutils-doc \  
gcc-doc \  
git \  
\--no-cache \  
&& git clone https://github.com/pgul/binkd.git /tmp/binkd-src \  
&& cd /tmp/binkd-src \  
&& cp mkfls/unix/* . \  
&& ./configure \  
&& make \  
&& make install \  
&& apk del build-base gcc abuild binutils binutils-doc gcc-doc git \  
&& rm -rf /tmp/binkd-src  
  
COPY scripts/poll_uplinks.sh /etc/periodic/hourly/poll_uplinks  
  
# override with something else to make the container poll your uplinks  
ENV UPLINKS=NONE  
  
VOLUME /config  
VOLUME /mail  
VOLUME /logs  
  
EXPOSE 24554  
ENTRYPOINT ["binkd"]  
  

