# Builds on top of wonderfall/Nextcloud and adds a script to remove the
permissions check.  
# Permissions cannot be set meaningfully if the Data directory is a windows
volume  
# Obtain base image  
FROM wonderfall/nextcloud:latest  
#change working dir  
WORKDIR /var  
#copy local files to image  
ADD . /var  
#RUN apt-get update \  
# && apt-get install nano  
RUN chmod 770 /var/RemPermCheck.sh \  
&& /var/RemPermCheck.sh  
  

