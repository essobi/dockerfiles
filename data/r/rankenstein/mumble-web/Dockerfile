FROM alpine:edge  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk add --no-cache git nodejs tini websockify  
  
COPY ./ /opt/mumble-web/  
  
WORKDIR /opt/mumble-web  
  
RUN npm install && npm run build  
  
EXPOSE 80  
ENV MUMBLE_SERVER=mumble.rankenste.in:64738  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD websockify --ssl-target --web /opt/mumble-web/dist 80 "$MUMBLE_SERVER"  

