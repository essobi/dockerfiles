FROM mhart/alpine-node:8.2.1  
LABEL maintainer="Code Computerlove"  
  
ENV BACKSTOPJS_VERSION="beta"  
ENV BACKSTOPJS_USER="backstop"  
ENV CHROME_PATH="/usr/bin/chromium-browser"  
# Dependencies & Chrome  
RUN \  
apk update && \  
apk upgrade && \  
apk add --no-cache --repository
https://dl-3.alpinelinux.org/alpine/edge/testing \  
make \  
grep \  
vips \  
vips-dev \  
fftw-dev \  
g++ \  
git \  
curl \  
python \  
bash \  
chromium && \  
rm -rf /var/cache/apk/*  
  
# BackstopJS  
RUN \  
echo "Installing BackstopJS v${BACKSTOPJS_VERSION}" && \  
yarn global add backstopjs@${BACKSTOPJS_VERSION}  
  
# Create user  
RUN addgroup ${BACKSTOPJS_USER} && adduser ${BACKSTOPJS_USER} -G
${BACKSTOPJS_USER} -h /home/${BACKSTOPJS_USER} -D  
RUN delgroup audio && addgroup audio -g 29 && addgroup ${BACKSTOPJS_USER}
audio  
USER ${BACKSTOPJS_USER}  
  
WORKDIR /src  
  
ENTRYPOINT ["backstop"]

