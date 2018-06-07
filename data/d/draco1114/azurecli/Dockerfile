# azurecli  
#  
# Azure command line tools with attached volume for data  
# and a nice bash prompt  
#  
# docker run -it --rm \  
# -v $(pwd)/azuredata:/data \  
# -w /data \  
# \--name azurecli \  
# draco1114/azurecli  
#  
FROM microsoft/azure-cli  
MAINTAINER Michael Thomas <draco1114@gmail.com>  
  
RUN curl
https://raw.githubusercontent.com/draco1114/dockerfiles/master/azurecli/bashrc
>> ~/.bashrc  

