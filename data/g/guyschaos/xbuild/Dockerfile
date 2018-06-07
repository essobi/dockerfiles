FROM guyschaos/abuild  
  
RUN apt-get update && \  
apt-get install -y vim \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV USER=root  
RUN echo "root:toor" | chpasswd  
RUN echo "appuser:appuser" | chpasswd  
RUN echo "appuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  

