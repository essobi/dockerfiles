FROM golang:alpine  
  
ENV GOPATH /usr/src/go  
ENV PATH $PATH:$GOPATH/bin  
  
RUN mkdir /config && \  
apk --no-cache add bash openssl git pv pigz xz bzip2  
  
RUN go get github.com/prasmussen/gdrive && \  
go install github.com/prasmussen/gdrive  
  
VOLUME /backup  
VOLUME /config  
VOLUME /backup  
  
COPY purge /usr/bin/purge  
COPY restore /usr/bin/restore  
COPY backup /usr/bin/backup  
  
RUN chmod +x /usr/bin/backup && chmod +x /usr/bin/purge && chmod +x
/usr/bin/restore  
  
CMD ["/usr/bin/backup"]  

