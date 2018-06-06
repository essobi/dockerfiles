FROM ethereumex/bootnode-registrar  
  
RUN useradd -ms /bin/bash dashboard  
USER dashboard  
  
WORKDIR /home/dashboard  
ADD app.json /home/dashboard/app.json  
ADD run.sh /home/dashboard/run.sh  
  
ADD updateNode.sh /home/dashboard/updateNode.sh  
RUN /bin/bash /home/dashboard/updateNode.sh  
  
ENTRYPOINT ["/bin/bash", "run.sh"]  

