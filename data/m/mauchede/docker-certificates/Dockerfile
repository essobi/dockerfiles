FROM alpine:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
OMGWTFSSL_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
curl \  
\  
&& apk add --no-cache --no-progress \  
bash \  
openssl \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/dumb-entrypoint/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/gosu/installer" | INSTALL_DIRECTORY="/usr/sbin" sh
-s -- install \  
\  
# Install paulczar/omgwtfssl  
\  
&& curl --location --output /usr/bin/generate-certs
"https://github.com/paulczar/omgwtfssl/raw/master/generate-certs" \  
&& chmod +x /usr/bin/generate-certs \  
\  
# Clean  
\  
&& apk del --no-progress \  
BUILD_DEPS  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

