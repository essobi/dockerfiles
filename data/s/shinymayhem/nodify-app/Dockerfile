FROM shinymayhem/node  
  
EXPOSE 80  
################ Begin Colby modify  
#  
#run any commands like this. they will be cached during the container build
process, and do not have access to shared volumes  
  
#  
############### End Colby modify  
  
#copy the startup script to the container  
COPY deploy/run.sh /opt/deploy/run.sh  
  
#This runs the script that was copied to the container once it is up and
running. This script has access to data on the shared volumes  
CMD /bin/bash /opt/deploy/run.sh  

