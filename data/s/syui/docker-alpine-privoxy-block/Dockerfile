FROM alpine:edge  
  
EXPOSE 8119  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' \  
>> /etc/apk/repositories && \  
apk --update add privoxy runit@testing  
  
COPY service /etc/service/  
  
CMD ["runsvdir", "/etc/service"]  

