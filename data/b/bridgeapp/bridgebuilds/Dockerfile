FROM node:6.10.3  
  
RUN apt-get update && apt-get install -y python-dev && \  
curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install awscli && \  
npm i -g kuda@0.0.10 serverless@1.23.0  
  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-3.0.3.778-linux.zip && \  
apt-get install unzip && \  
unzip sonar-scanner-cli-3.0.3.778-linux.zip -d /usr/local/sonar-scanner  
  
ENV PATH="/usr/local/sonar-scanner/sonar-scanner-3.0.3.778-linux/bin:${PATH}"  
CMD /bin/bash  

