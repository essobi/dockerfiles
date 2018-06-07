FROM larsks/alpine-s6  
  
RUN apk add transmission-daemon  
VOLUME /transmission  
COPY ensure_dirs.sh /docker/entrypoint.d/ensure_dirs  
COPY services /services  

