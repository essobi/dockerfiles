FROM node:6.2.2  
RUN apt-get update && apt-get install awscli -y  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y python-setuptools python-dev libffi-dev libssl-dev git
sshpass tree  
RUN easy_install pip  
RUN pip install cryptography  
RUN pip install ansible==2.4.0.0  
  
RUN curl -SLO "https://s3.amazonaws.com/codeship-jet-releases/1.19.3/jet-
linux_amd64_1.19.3.tar.gz"  
RUN tar -xaC /usr/local/bin -f jet-linux_amd64_1.19.3.tar.gz  
RUN chmod +x /usr/local/bin/jet  
RUN wget http://stedolan.github.io/jq/download/linux64/jq  
RUN chmod +x ./jq  
RUN cp jq /usr/bin  

