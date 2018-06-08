  
FROM mirkokiefer/ubuntu-base  
  
ADD scripts /scripts  
RUN bash /scripts/install_node.sh  
  
RUN echo "export NODE_PATH=/usr/local/lib/node_modules" >> ~/.bashrc  

