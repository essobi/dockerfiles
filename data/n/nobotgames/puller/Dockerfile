FROM docker  
  
# must do -v /var/run/docker.sock:/var/run/docker.sock  
VOLUME /var/run/docker.sock:/var/run/docker.sock  
  
COPY . /home/main  
  
CMD sh /home/main/run.sh  

