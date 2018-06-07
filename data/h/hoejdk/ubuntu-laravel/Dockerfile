FROM ubuntu:17.04  
RUN apt-get update  
RUN apt-get install -y composer php7.0 php7.0-mbstring php7.0-curl php7.0-gd
php7.0-dom phpunit nodejs npm libnotify-bin nano curl unzip python  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN aws configure set default.region eu-west-1

