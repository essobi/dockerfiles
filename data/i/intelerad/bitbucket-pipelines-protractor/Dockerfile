FROM intelerad/bitbucket-pipeline-
browsers@sha256:53ade1a51da91274b8b96048b7f6000bce9ed3e7d2dc3074bbf4584c02fe5aad  
MAINTAINER "Intelerad Medical Systems"  
ENV NVM_DIR /usr/local/nvm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash  
ENV NODE_VERSION v9.3.0  
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm
use --delete-prefix $NODE_VERSION"  
  
ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH  
  
RUN npm install -g protractor@5.2.2 jasmine@2.8.0 jasmine-spec-reporter@4.2.1
&& webdriver-manager update  
  
RUN add-apt-repository ppa:mc3man/trusty-media && \  
apt-get update && \  
apt-get install -y zip ffmpeg python-pip && \  
apt-get clean  
  
RUN pip install --upgrade awscli==1.14.5 s3cmd==2.0.1 python-magic  

