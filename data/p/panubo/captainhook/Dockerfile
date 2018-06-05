FROM golang:1.4.3  
EXPOSE 8080  
WORKDIR /go/src/app  
  
RUN git clone https://github.com/bketelsen/captainhook.git /go/src/app && rm
-rf .git && \  
go-wrapper download && \  
go-wrapper install && \  
mkdir /config && \  
useradd --home-dir /go/src/app captain  
  
COPY entry.sh /  
  
USER captain  
  
ENTRYPOINT ["/entry.sh"]  
  
CMD ["/go/bin/app", "-echo", "-listen-addr", "0.0.0.0:8080", "-configdir",
"/config"]  

