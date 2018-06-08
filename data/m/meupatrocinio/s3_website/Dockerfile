FROM node:8  
RUN apt-get update && \  
apt-get install -y apt-transport-https curl && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y openjdk-7-jre-headless build-essential python-dev ruby-full
yarn git bash sudo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \  
pip install awscli && \  
aws configure set preview.cloudfront true  
  
RUN mkdir /app  
  
WORKDIR /app  
  
RUN npm install -g typescript  
RUN gem install s3_website  
  
USER root  
RUN s3_website install  
  
CMD ["/bin/bash"]  

