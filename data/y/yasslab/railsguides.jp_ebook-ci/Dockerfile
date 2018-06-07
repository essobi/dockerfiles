FROM ruby:2.4.1-alpine  
  
ENV LANG C.UTF-8  
  
# install Re:VIEW environment  
## for pdf  
RUN mkdir /texlive  
COPY texlive.profile /texlive  
RUN apk --update \--no-cache add wget ca-certificates perl xz && \  
cd /texlive && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk && \  
apk add glibc-2.25-r0.apk && \  
wget http://mirror.unl.edu/ctan/systems/texlive/tlnet/install-tl-unx.tar.gz &&
\  
tar xvf install-tl-unx.tar.gz && \  
cd install-tl* && \  
./install-tl \--profile /texlive/texlive.profile \--repository
http://ctan.math.utah.edu/ctan/tex-archive/systems/texlive/tlnet/ && \  
cd / && \  
rm -rf /texlive  
RUN apk --update \--no-cache add build-base git imagemagick-dev ghostscript
zip openjdk8-jre-base  

