FROM node:4  
# install the required dependencies to compile native extensions  
# ENV USER_ID 500  
# ENV GROUP_ID 500  
# ENV user ec2-user  
# RUN groupadd --system $user --gid $GROUP_ID && useradd --system --create-
home --gid $user --uid $USER_ID $user  
ENV PYTHONIOENCODING=UTF-8  
COPY . /home/$user/  
WORKDIR /home/$user  
  
# VOLUME /usr/src/app  
# WORKDIR /usr/src/app  
RUN npm init -y  
RUN npm install -g serverless@0.5.6  
RUN npm install -g serverless-optimizer-plugin@2.5.1 serverless-cors-
plugin@0.4.1  
RUN npm install -g aws-dynamodb omit-empty request url-parse bluebird
dynamodb-marshaler moment node-uuid  
RUN npm install -g bluebird nodemailer async-foreach jsonwebtoken nodemailer-
mandrill-transport nodemailer-sendgrid-transport nodemailer-ses-transport  
RUN npm install -g akismet-api async-foreach slack-notify string  
RUN npm install -g request omit-empty async-foreach isgd string validator
async randomstring s3 node-rules slack-notify  
RUN npm install -g xml-objtree foreach aws-dynamodb url-parse auth0  
  
RUN mkdir ~/.aws  
RUN mkdir ~/app  
  
RUN ln -sf /usr/share/zoneinfo/Australia/Melbourne localtime  
  
WORKDIR /home/node/app  
  
CMD ["ls"]  

