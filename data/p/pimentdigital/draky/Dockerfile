FROM ubuntu  
MAINTAINER Mac Oosthuizen <mac@piment.digital>  
  
RUN sudo apt-get update  
RUN sudo sudo apt-get install -y python-software-properties software-
properties-common  
RUN sudo add-apt-repository ppa:chris-lea/node.js  
RUN sudo apt-get update  
RUN sudo apt-get install -y git python g++ make nodejs  
RUN sudo npm install -g bower gulp  
RUN sudo npm install -g http-server  
  
ADD ./ /opt/site/  
WORKDIR /opt/site  
  
RUN make setup  
RUN make build  
  
CMD ["http-server", "build/"]  
  
EXPOSE 8080  

