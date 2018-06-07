FROM alpine:edge  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
RUN apk --no-cache add ttf-dejavu ttf-droid ttf-freefont ttf-liberation ttf-
ubuntu-font-family ttf-opensans font-adobe-100dpi  
RUN apk --no-cache add firefox  
ENV TZ=Europe/Berlin  
VOLUME /output  
WORKDIR /output  
  
ENTRYPOINT ["firefox"]  

