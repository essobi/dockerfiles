FROM shippableimages/ubuntu1204_nodejs  
  
ENV DEFAULT_NODE_VERSION 5.8.0  
RUN apt-get update && apt-get install -y \  
default-jre \  
zip \  
wget  
  
RUN wget
http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-3ubuntu0.4_amd64.deb
\  
&& dpkg -i libicu52_52.1-3ubuntu0.4_amd64.deb \  
&& rm libicu52_52.1-3ubuntu0.4_amd64.deb  
  
RUN wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz -O
/tmp/dynamodb_local_latest.tar.gz  
  
RUN tar -xzf /tmp/dynamodb_local_latest.tar.gz -C /tmp  
  
RUN . ~/.nvm/nvm.sh && nvm install 0.10  
RUN . ~/.nvm/nvm.sh && nvm install 0.12  
RUN . ~/.nvm/nvm.sh && nvm install 5.3.0  
RUN . ~/.nvm/nvm.sh && nvm install 5.4.0  
RUN . ~/.nvm/nvm.sh && nvm install ${DEFAULT_NODE_VERSION}  
  
RUN . ~/.nvm/nvm.sh && nvm use ${DEFAULT_NODE_VERSION}  
  
RUN . ~/.nvm/nvm.sh && nvm use ${DEFAULT_NODE_VERSION} && npm -g install
npm@latest  
RUN . ~/.nvm/nvm.sh && nvm use ${DEFAULT_NODE_VERSION} && npm -g install
typings  
RUN . ~/.nvm/nvm.sh && nvm use ${DEFAULT_NODE_VERSION} && npm -g install gulp  
RUN . ~/.nvm/nvm.sh && nvm use ${DEFAULT_NODE_VERSION} && npm -g install
mountebank  
  
ADD deploy/ /deploy  
ADD deploy.sh /  
RUN chmod +x /deploy.sh  

