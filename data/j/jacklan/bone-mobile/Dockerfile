FROM node  
MAINTAINER jack <lanjackg2003@qq.com>  
RUN apt-get update && apt-get install expect -y  
RUN npm install -g bnpm --registry=https://npm.aliplus.com/api  
RUN chown -R $(whoami) /usr/local/bin  
RUN chown -R $(whoami) /usr/local/lib  
WORKDIR /build  
CMD ["/bin/bash"]

