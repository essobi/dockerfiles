FROM nginx:stable-alpine  
  
RUN apk --no-cache add ca-certificates wget tar \  
&& wget -O freeboard.tar.gz
https://api.github.com/repos/Freeboard/freeboard/tarball/master \  
&& tar -xzvf freeboard.tar.gz -C /usr/share/nginx/html \--strip-components=1  

