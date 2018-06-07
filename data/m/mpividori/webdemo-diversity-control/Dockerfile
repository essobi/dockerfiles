FROM sinclab/webdemo-base-matlab  
MAINTAINER Milton Pividori <mpividori@sinc.unl.edu.ar>  
  
# Web Demo Builder - Base Docker image for Diversity Control  
# Install base packages  
RUN DEBIAN_FRONTEND=noninteractive \  
dpkg --add-architecture i386 && \  
apt-get update && apt-get install -y \  
libc6-dbg \  
libc6:i386 \  
libc6-dbg:i386 \  
texlive && \  
apt-get clean && apt-get autoclean  
  

