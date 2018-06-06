FROM alpine:latest  
RUN echo '#!/bin/sh' > /usr/bin/dsmoke.sh \  
&& echo 'if [ -n "$DSMOKE_LISTEN_PORT" ]; then
LISTEN_PORT="$DSMOKE_LISTEN_PORT" ; else LISTEN_PORT=8080 ; fi' >>
/usr/bin/dsmoke.sh \  
&& echo 'while true ; do echo -e "HTTP/1.1 200 OK\r\n\r\nOK" | nc -l -p
${LISTEN_PORT} ; done' >> /usr/bin/dsmoke.sh \  
&& chmod 750 /usr/bin/dsmoke.sh  
  
CMD [ "/usr/bin/dsmoke.sh" ]  
  

