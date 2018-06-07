FROM node:alpine  
  
LABEL author "Korviakov Andrey"  
LABEL maintainer "4lifenet@gmail.com"  
  
COPY bin/ /bin  
  
RUN apk add --no-cache \  
bash \  
coreutils \  
dbus \  
curl \  
firefox-esr \  
fontconfig \  
ttf-freefont \  
xvfb \  
&& npm install slimerjs  
  
ENV SLIMERDIR=/node_modules/slimerjs/src  
ENV SLIMERJSLAUNCHER=/usr/bin/firefox  
ENV PATH="/node_modules/.bin/:${PATH}"  
WORKDIR /src  
  
ENTRYPOINT ["xvfb-run", "slimerjs"]  

