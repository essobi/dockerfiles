FROM ubuntu  
MAINTAINER wh11e7rue<wh11e7rue@icloud.com>  
  
RUN apt-get update \  
&& apt-get install -y emacs  
  
COPY init.el /root/.emacs.d/  
COPY bashrc /root/.bashrc  
  
CMD bash  

