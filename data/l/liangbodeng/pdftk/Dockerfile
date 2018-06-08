FROM alpine:3.5  
  
RUN apk update && apk upgrade \  
&& apk add pdftk \  
&& mkdir /pdf  
  
WORKDIR /pdf  
VOLUME /pdf  
  
ENTRYPOINT [ "pdftk" ]  
  

