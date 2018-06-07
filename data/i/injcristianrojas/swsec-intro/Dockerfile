FROM alpine:latest  
  
RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk add --update bash openjdk8 maven@testing supervisor vim nano  
  
COPY . /app  
WORKDIR /app  
RUN ["mvn", "site", "install"]  
  
RUN chmod +x /app/go.sh  
RUN cp /app/supervisord.conf /etc/supervisord-default.conf  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon", "--configuration",
"/etc/supervisord-default.conf"]  

