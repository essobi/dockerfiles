FROM maven:3.3.3-jdk-8  
  
WORKDIR /root  
  
  
##################################################  
# Install AWS CLI  
##################################################  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" \  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
  
COPY /root/.aws/config /root/.aws/config  
  
  
##################################################  
# Install AWS API Gateway Importer  
##################################################  
RUN git clone https://github.com/awslabs/aws-apigateway-importer.git \  
&& cd aws-apigateway-importer && mvn assembly:assembly  
  
  
COPY /entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["bash", "/entrypoint.sh"]  

