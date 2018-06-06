FROM pistatium/docker-compose:1.11.2  
  
RUN pip install virtualenv && virtualenv cli && cli/bin/pip install awscli
awsebcli  
  
ENV PATH $PATH:/cli/bin  

