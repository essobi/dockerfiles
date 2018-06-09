FROM node:alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
CHOKIDAR_USEPOLLING=true  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress \  
binutils \  
ca-certificates \  
curl \  
fftw-dev \  
g++ \  
git \  
gpgme \  
make \  
openssh-client \  
python \  
&& apk add --no-cache --no-progress --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing \  
vips-dev \  
\  
# Install api-platform/client-generator \  
\  
&& yarn global add \  
@api-platform/client-generator \  
\  
# Install angular/cli \  
\  
&& yarn global add \  
@angular/cli \  
\  
# Install facebookincubator/create-react-app  
\  
&& yarn global add \  
create-react-app \  
\  
# Install prettier/prettier  
\  
&& yarn global add \  
prettier \  
\  
# Install sgerrand/alpine-pkg-glibc  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/sgerrand/alpine-pkg-glibc/latest" | xargs) \  
&& curl --location --output /etc/apk/keys/sgerrand.rsa.pub
"https://github.com/sgerrand/alpine-pkg-glibc/raw/master/sgerrand.rsa.pub" \  
&& curl --location --output /tmp/glibc.apk
"https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" \  
&& apk add /tmp/glibc.apk \  
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
# Install zeit/serve  
\  
&& yarn global add \  
serve \  
\  
# Clean  
\  
&& rm -f -r \  
/tmp/*  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

