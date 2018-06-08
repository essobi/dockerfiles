FROM ubuntu:16.04  
RUN apt-get update && apt-get install curl -y  
  
RUN curl -L https://bootstrap.saltstack.com | sh -s -- -M -X stable  
  
CMD ["salt-master", "--log-level=debug"]  

