FROM ubuntu:14.04.1  
MAINTAINER Luis Santos "luis.santos@logicnow.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common apt-transport-https  
RUN apt-add-repository ppa:ansible/ansible  
RUN apt-get update  
RUN apt-get install -y ansible python-pip curl  
  
WORKDIR /logicnow  
  
ADD logicnow /logicnow  
  
RUN ansible-playbook /logicnow/ansible/dynamodb/deploy.yml -c local  
RUN chmod +x /logicnow/tools/runDynamo.sh  
  
ENTRYPOINT /logicnow/tools/runDynamo.sh  

