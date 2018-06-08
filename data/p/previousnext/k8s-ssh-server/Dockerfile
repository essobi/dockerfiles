FROM golang:1.8  
ADD Makefile /go/Makefile  
ADD hack /go/hack  
ADD src /go/src  
ADD vendor /go/vendor  
  
RUN make server cli github-sync && \  
mv bin/linux/cli/ssh-cli /usr/local/bin/cli && \  
mv bin/linux/cli/github-sync /usr/local/bin/github-sync && \  
mv bin/linux/server/ssh-server /usr/local/bin/ssh-server && \  
chmod a+x /usr/local/bin/cli && \  
chmod a+x /usr/local/bin/ssh-server && \  
chmod a+x /usr/local/bin/github-sync  
  
# Cleanup.  
RUN rm -fR /go  
  
CMD ["ssh-server"]  

