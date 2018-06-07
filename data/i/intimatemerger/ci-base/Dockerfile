FROM python:2.7.12  
LABEL maintainer "mats116 <mats.kazuki@gmail.com>"  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y --no-install-recommends \  
unzip \  
mysql-client \  
nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
npm install -g gulp@3.9.1  
  
# Install the AWS CLI Using the Bundled Installer  
# http://docs.aws.amazon.com/ja_jp/cli/latest/userguide/awscli-install-
bundle.html  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
rm -rf awscli-bundle.zip awscli-bundle  
  
CMD ["/bin/bash"]  

