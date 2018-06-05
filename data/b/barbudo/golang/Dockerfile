FROM m0sth8/base:latest  
  
  
ENV GOLANG_VERSION 1.3.3  
RUN /build/golang.sh \  
&& apt-get update \  
&& /build/cvs.sh \  
&& /build/finalize.sh  
  
RUN mkdir '/go' '/go/bin' '/go/src'  
ENV PATH
/usr/local/go/bin:/go/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin  
ENV GOROOT /usr/local/go  
ENV GOPATH /go

