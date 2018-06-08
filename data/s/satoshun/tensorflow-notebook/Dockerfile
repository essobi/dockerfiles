FROM satoshun/jupyter  
  
MAINTAINER SatoShun <shun.sato1@gmail.com>  
  
USER root  
  
RUN apt-get clean && apt-get upgrade -y && apt-get update -y --fix-missing  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq python3-numpy
python3-scipy  
  
RUN pip3 install -U wheel six sklearn pandas  
RUN pip3 install --upgrade
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.6.0-cp34-none-
linux_x86_64.whl  

