#*******************************************************************************  
#Dockerfile  
#*******************************************************************************  
  
#Purpose:  
#This file describes the operating system prerequisites for SHBAAM, and is
used  
#by the Docker software.  
#Author:  
#Cedric H. David, 2018-2018  
  
  
#*******************************************************************************  
#Usage  
#*******************************************************************************  
#docker build -t ubuntu:shbaam -f Dockerfile . #Create image  
#docker run --rm --name ubuntu_shbaam -it ubuntu:shbaam #Run image in
container  
#docker save -o ubuntu_shbaam.tar ubuntu:shbaam #Save a copy of image  
#docker load -i ubuntu_shbaam.tar #Load a saved image  
  
  
#*******************************************************************************  
#Operating System  
#*******************************************************************************  
FROM tdhttt/shbaam:install  
  
#*******************************************************************************  
#Copy files into Docker image (this ignores the files listed in .dockerignore)  
#*******************************************************************************  
WORKDIR /home/shbaam/  
COPY . .  
WORKDIR /home/shbaam/tst  
  
RUN /bin/bash ./tst_pub_dwnl_David_etal_201x_SER.sh  
RUN /bin/bash ./tst_pub_repr_David_etal_201x_SER.sh  

