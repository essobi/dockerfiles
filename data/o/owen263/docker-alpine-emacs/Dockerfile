FROM alpine:3.7 AS build-stage  
WORKDIR /root  
ADD https://github.com/silencej/wcfShells/archive/master.zip /root  
RUN unzip /root/master.zip  
  
FROM alpine:3.7  
MAINTAINER Iku Iwasa "iku.iwasa@gmail.com"  
RUN apk update && apk add ca-certificates emacs xclip  
  
WORKDIR /root  
  
COPY \--from=build-stage /root/wcfShells-master /root/wcfShells  
COPY init.el /root/.emacs.d/  
COPY entrypoint.sh /  
  
RUN emacs -batch -l /root/.emacs.d/init.el  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "emacs" ]  

