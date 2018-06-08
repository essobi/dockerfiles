FROM mhart/alpine-node:9.5.0  
RUN apk add --no-cache wget git make gnuplot ghostscript fontconfig ca-
certificates openssl  
  
RUN mkdir /tmp/install-tl-unx  
  
WORKDIR /tmp/install-tl-unx  
  
COPY texlive.profile .  
  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
apk --no-cache -X https://apkproxy.herokuapp.com/sgerrand/alpine-pkg-glibc add
glibc glibc-bin  
  
RUN apk --no-cache add perl wget xz tar && \  
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \  
tar --strip-components=1 -xvf install-tl-unx.tar.gz && \  
./install-tl --profile=texlive.profile && \  
tlmgr install collection-latex collection-latexextra && \  
cd && rm -rf /tmp/install-tl-unx  
  
RUN tlmgr install bytefield algorithms algorithm2e ec fontawesome epstopdf
latexmk collection-bibtexextra collection-plaingeneric collection-
fontsrecommended && mkdir /workdir && cd /workdir  
  
ENV PATH="/usr/local/texlive/2017/bin/x86_64-linux:${PATH}"  
WORKDIR /workdir  
  
VOLUME ["/workdir"]  

