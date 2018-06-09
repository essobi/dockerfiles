FROM stevensciriha/ubuntucustom_orig  
  
RUN apt-get update  
  
RUN apt-get install openssh-server -y  
#  
RUN service ssh restart  
# overwrite this with 'CMD []' in a dependent Dockerfile  
ENTRYPOINT /bin/bash  

