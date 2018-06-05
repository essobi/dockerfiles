FROM microsoft/dotnet:latest  
  
RUN apt-get clean && apt-get update  
RUN yes | apt-get upgrade  
RUN yes | apt-get install wget tar unzip  
  
# s6 overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.17.2.0/s6-overlay-amd64.tar.gz
/tmp/s6-overlay.tar.gz  
RUN tar xvfz /tmp/s6-overlay.tar.gz -C /; \  
rm -rf /etc/s6  
  
RUN wget https://releases.hashicorp.com/consul-template/0.14.0/consul-
template_0.14.0_linux_386.zip; \  
unzip consul-template_0.14.0_linux_386.zip; \  
mv consul-template /bin/consul-template  

