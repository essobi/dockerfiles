FROM tsuzu/gmusic  
  
WORKDIR /tmp  
RUN apt-get install -y language-pack-ja  
RUN wget https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz &&
tar zxvf go*.tar.gz  
RUN mv go*/ /usr/local/go && mkdir /root/go  
ENV GOPATH "/root/go"  
ENV GOROOT "/usr/local/go"  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
RUN go get github.com/cs3238-tsuzu/recs4m  
RUN cp $GOPATH/src/github.com/cs3238-tsuzu/recs4m/upload.sh /root  
RUN chmod +x /root/upload.sh  
WORKDIR $GOPATH/src/github.com/cs3238-tsuzu/recs4m  
EXPOSE 80  
CMD ["recs4m", "--upload-script", "/root/upload.sh"]

