FROM alpine  
  
WORKDIR /root  
  
EXPOSE 8080  
CMD /root/start.sh  
  
ENV GOPATH $HOME/gohome  
ENV GOBIN $HOME/gohome/bin  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk update && \  
apk add bash go nodejs git make python && \  
npm install -g bower && \  
mkdir -p /root/frontend $GOPATH/bin $GOPATH/src  
  
COPY main.sh /etc/profile.d  
COPY frontend /root/frontend  
COPY main.go start.sh Makefile /root/  
  
RUN make main && \  
apk del git python make && \  
rm -rf /var/cache/apk/* /root/Makefile /root/main.go  

