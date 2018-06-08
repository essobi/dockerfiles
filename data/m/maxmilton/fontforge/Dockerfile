# Run FontForge in a container  
#  
# Build image:  
# docker build -t local/fontforge .  
#  
# Update:  
# docker build --no-cache -t local/fontforge .  
#  
FROM
alpine:edge@sha256:6fa3225360ea1a48aaee4ca87de66e8e12b9a4f749f37acc7b4b5b9cc3d91b13  
  
RUN set -xe \  
&& addgroup -g 7027 -S fontforge \  
&& adduser -D -u 7027 -S -h /home/fontforge -s /sbin/nologin -G fontforge
fontforge \  
&& adduser fontforge video \  
&& apk add --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing \  
fontforge \  
mesa-dri-intel \  
mesa-gl \  
ttf-dejavu \  
unifont  
  
# run as non privileged user  
USER fontforge  
WORKDIR /home/fontforge  
  
ENTRYPOINT ["/usr/bin/fontforge"]  
CMD ["about:blank"]  

