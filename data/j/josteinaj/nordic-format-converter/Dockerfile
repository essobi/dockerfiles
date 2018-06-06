FROM josteinaj/nordic-migrator  
  
MAINTAINER Jostein Austvik Jacobsen  
  
WORKDIR /home/root/  
  
# Install Nordic EPUB3/DTBook Migrator  
ADD script /home/root/script/  
  
# Declare the mount point for the book archive  
#VOLUME /media/archive  
  
ENTRYPOINT ["/home/root/script/run.sh"]  
#CMD ["/home/root/daisy-pipeline/cli/dp2", "help"]  

