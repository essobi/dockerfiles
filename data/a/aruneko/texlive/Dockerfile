FROM frolvlad/alpine-glibc  
  
ENV PATH $PATH:/usr/local/texlive/2017/bin/x86_64-linux  
  
COPY texlive.profile /tmp  
  
RUN apk add \--no-cache perl py-pygments && \  
apk add \--no-cache --virtual .setup_deps wget xz && \  
cd /tmp && \  
wget -nv -O install-tl.tar.gz
http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \  
mkdir install-tl && \  
tar -xzf install-tl.tar.gz -C install-tl \--strip-components=1 && \  
cd install-tl/ && \  
( ./install-tl \--persistent-downloads --profile /tmp/texlive.profile || \  
./install-tl \--persistent-downloads --profile /tmp/texlive.profile || \  
./install-tl \--persistent-downloads --profile /tmp/texlive.profile ) && \  
cd ../ && \  
rm -rf install-tl.tar.gz install-tl && \  
mkdir /texsrc  
  
VOLUME /texsrc  
  
WORKDIR /texsrc  
  
CMD ["/bin/ash"]  

