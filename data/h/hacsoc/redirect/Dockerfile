FROM alpine  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk add --update nginx dockerize@testing && rm -rf /var/cache/apk/*  
  
COPY run.sh /  
COPY default.conf.tmpl /app/default.conf.tmpl  
  
ENV REDIRECT **None**  
  
CMD ["/run.sh"]  

