FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y curl openssh-client  
ADD setup setup  
RUN chmod +x setup  
CMD "./setup"  
  
#docker run -e ETCD_API=172.17.42.1:4001 cakk/agent  

