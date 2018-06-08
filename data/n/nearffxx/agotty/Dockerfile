FROM alpine  
  
RUN apk add --no-cache bash fakeroot git vim py-pip python-dev openssl-dev
libffi-dev linux-headers gcc go musl-dev make tmux  
  
ADD requirements.txt /  
  
RUN pip install -r requirements.txt  
  
ENV GOROOT /usr/lib/go  
  
ENV GOPATH /gopath  
  
ENV GOBIN /gopath/bin  
  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
RUN go get github.com/yudai/gotty  
  
CMD TERM=xterm HOME=root exec gotty -w tmux new -A -s gotty bash  

