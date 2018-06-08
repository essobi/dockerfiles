FROM debian:9.4  
RUN apt-get update  
RUN apt-get install lsb-release curl apt-transport-https gnupg vim -y  
ENV CLOUD_SDK_REPO cloud-sdk-stretch  
RUN echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee
-a /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
RUN apt-get update && apt-get install google-cloud-sdk kubectl -y  
ADD cleanup.sh /cleanup.sh  
RUN chmod +x /cleanup.sh  
ENTRYPOINT [ "/cleanup.sh" ]  

