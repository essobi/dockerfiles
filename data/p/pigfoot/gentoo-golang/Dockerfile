FROM pigfoot/gentoo-base  
MAINTAINER pigfoot <pigfoot@gmail.com>  
  
RUN ACCEPT_KEYWORDS="~amd64" emerge -v dev-lang/go  
RUN ["mkdir", "-p", "/go"]  
  
ENV GOROOT /usr/lib/go  
ENV GOPATH /go  
ENV PATH ${GOPATH}/bin:${GOROOT}/bin:${PATH}  
WORKDIR ${GOPATH}  

