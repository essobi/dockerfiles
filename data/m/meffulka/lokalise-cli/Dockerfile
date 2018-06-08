FROM alpine:3.7  
LABEL maintainer="Alekseii Erokhin <zmeffulka@gmail.com>"  
  
RUN apk add --no-cache git coreutils openssh zip  
  
COPY lokalise /usr/local/bin/  
  
RUN chmod 755 /usr/local/bin/lokalise  
  
CMD /bin/sh  

