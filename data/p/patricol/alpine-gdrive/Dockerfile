#Loosely based on https://github.com/mitcdh/docker-google-drive-ocamlfuse and
https://github.com/MartyTremblay/docker-google-drive-ocamlfuse  
FROM patricol/compile:gdrive as gdrive  
FROM alpine:latest  
  
COPY \--from=gdrive /google-drive-ocamlfuse /bin/google-drive-ocamlfuse  
COPY entrypoint.sh /  
COPY default_config /  
  
RUN apk add \--no-cache fuse libgmpxx sqlite-libs libcurl libressl ncurses-
libs && \  
chmod +x /entrypoint.sh && \  
mkdir -p ~/.gdfuse/ && \  
ln -s /config ~/.gdfuse/default  
  
VOLUME /config  
VOLUME /data  
  
ENTRYPOINT ["/entrypoint.sh"]

