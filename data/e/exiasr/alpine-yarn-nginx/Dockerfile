FROM nginx:1.13.9-alpine  
LABEL maintainer="Michael Lin <michaellin@ualberta.ca>"  
# Install nvm with node and npm  
RUN apk add \--no-cache \--repository
http://nl.alpinelinux.org/alpine/edge/main libuv \  
&& apk add \--no-cache \--update-cache \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/main nodejs=8.9.4-r0 nodejs-npm=8.9.4-r0 \  
&& apk add \--no-cache \--update-cache \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/community yarn=1.5.1-r0 \  
&& echo "NodeJS Version:" "$(node -v)" \  
&& echo "NPM Version:" "$(npm -v)" \  
&& echo "Yarn Version:" "$(yarn -v)"  

