FROM python:alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
GIT_UP_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
curl \  
&& apk add --no-cache --no-progress \  
ca-certificates \  
git \  
openssh-client \  
\  
# Install msiemens/PyGitUp  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/msiemens/pygitup/${GIT_UP_VERSION}" | xargs) \  
&& pip install \  
"git-up==${GIT_UP_VERSION}" \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/dumb-entrypoint/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/dumb-init/installer" | INSTALL_DIRECTORY="/usr/sbin"
sh -s -- install \  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/gosu/installer" | INSTALL_DIRECTORY="/usr/sbin" sh
-s -- install \  
\  
# Clean  
\  
&& apk del --no-progress \  
BUILD_DEPS \  
&& rm -f -r \  
/root/.cache \  
/tmp/*  
  
ENTRYPOINT [ "dumb-init" , "--" , "dumb-entrypoint" ]  

