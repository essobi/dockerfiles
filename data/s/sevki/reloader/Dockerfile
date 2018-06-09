FROM invokr/cgit  
  
RUN yum update -y && yum upgrade -y && yum install go -y  
  
RUN git clone git://git.zx2c4.com/cgit && cd cgit && git submodule init && git
submodule update \  
&& make NO_LUA=1 && make install && cd .. && rm -Rf cgit  
  
RUN mkdir -p /go/src/reloader  
ADD main.go /go/src/reloader/main.go  
ADD cgitrc /etc/cgitrc  
ENV GOPATH /go  
RUN go get reloader  
  
CMD /go/bin/reloader

