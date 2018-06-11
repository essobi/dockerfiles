FROM praekeltfoundation/vumi  
MAINTAINER Praekelt Foundation <dev@praekeltfoundation.org>  
  
# Install nodejs 0.10 from the Debian repo & make executable available as
'node'  
RUN apt-get-install.sh nodejs && \  
update-alternatives --install /usr/bin/node node /usr/bin/nodejs 50  
  
ENV VXSANDBOX_VERSION "0.6.1"  
RUN pip install vxsandbox==$VXSANDBOX_VERSION  
  
ENV WORKER_CLASS "vxsandbox.worker.StandaloneJsFileSandbox"  

