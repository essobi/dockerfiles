FROM openeye/oenotebook  
  
MAINTAINER OpenEye <mattg@eyesopen.com>  
  
ENV OE_LICENSE /mnt/vol0/oe_license.txt  
  
# oe-user is our user  
RUN useradd -m -s /bin/bash oe-user  
ADD start_jupyter.bash /tmp/start_jupyter.bash  
USER oe-user  
WORKDIR /home/oe-user/  
  
CMD /bin/bash /tmp/start_jupyter.bash  

