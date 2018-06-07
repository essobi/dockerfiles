#  
# Node.js  
#  
# This Dockerfile installs the latest Node.js version  
# from the Alpine Linux edge repository.  
#  
FROM alpine  
MAINTAINER Marcus André <hello@marcusandre.de>  
  
# install `node`  
RUN apk add nodejs \  
\--update \  
\--no-cache \  
\--update-cache \  
\--allow-untrusted \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/main/  
  
# start `node`  
CMD ["node"]  

