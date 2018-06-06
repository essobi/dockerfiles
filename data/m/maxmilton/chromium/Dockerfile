# Run the Chromium browser in a container  
#  
# Build or update image:  
# docker build --no-cache -t local/chromium .  
#  
# TODO: Chromium on Alpine Linux is poorly maintained, consider switching back
to Debian  
FROM
alpine:edge@sha256:6fa3225360ea1a48aaee4ca87de66e8e12b9a4f749f37acc7b4b5b9cc3d91b13  
  
RUN set -xe \  
&& addgroup -g 6006 -S chromium \  
&& adduser -D -u 6006 -S -h /home/chromium -s /sbin/nologin -G chromium
chromium \  
&& adduser chromium audio \  
&& adduser chromium video \  
&& apk add --no-cache --virtual .system-deps \  
tzdata \  
&& apk add --no-cache \  
chromium \  
libcanberra-gtk3 \  
mesa-dri-intel \  
mesa-gl \  
&& cp /usr/share/zoneinfo/UTC /etc/localtime \  
&& echo "UTC" > /etc/timezone \  
&& apk del .system-deps  
  
# override default launcher  
COPY chromium /usr/lib/chromium/chromium-launcher.sh  
  
# custom chromium flags  
COPY default.conf /etc/chromium/default.conf  
  
# run as non privileged user  
USER chromium  
  
ENTRYPOINT ["/usr/bin/chromium-browser"]  
CMD ["about:blank"]  

