FROM ubuntu:14.04  
RUN apt-get update  
  
RUN apt-get install -y curl  
  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && echo "deb
http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee
/etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key
add -  
RUN sudo apt-get update && sudo apt-get install -y google-cloud-sdk  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
ADD run.sh /run.sh  
ADD run.js /run.js  
  
# Run the command on container startup  
CMD ["node","/run.js"]

