FROM node:8  
USER root  
RUN apt-get update && apt-get install -y apt-utils  
RUN apt-get -y install python-dev  
RUN apt-get -y install python3-dev  
RUN apt-get -y install curl  
RUN apt-get -y install unzip  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN yarn global add serverless  
RUN yarn global add knex

