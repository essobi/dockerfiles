FROM fedora  
MAINTAINER Brian (bex) Exelbierd <bex@pobox.com>  
  
# Install the appropriate software  
RUN dnf install -y npm tar bzip2 freetype fontconfig  
RUN npm install -g prez  
RUN npm install -g phantomjs  
  
# Setup working directory  
WORKDIR /workdir  
  
# Add a prez user - this prevents it from looking in ~/  
RUN useradd prez -M -d /workdir  
USER prez  
  
# Labels - today atomic run will not work :( so use INSTALL  
LABEL RUN docker run --rm=true \--privileged -u \${SUDO_UID}:\${SUDO_GID} -p
9000:9000 -v `pwd`:/workdir \${IMAGE}  
LABEL INSTALL docker run --rm=true \--privileged -u \${SUDO_UID}:\${SUDO_GID}
-p 9000:9000 -v `pwd`:/workdir \${IMAGE}  
  
ENTRYPOINT ["/usr/bin/prez"]  

