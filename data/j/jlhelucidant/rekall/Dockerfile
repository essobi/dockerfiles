FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y python3 python3-pip libncurses-dev &&
\  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install virtualenv  
  
RUN virtualenv /root/rekall-1.7.1 && /root/rekall-1.7.1/bin/pip3 install
rekall-agent==1.7.1 rekall==1.7.1  
  
CMD /bin/bash --rcfile /root/rekall-1.7.1/bin/activate  
  

