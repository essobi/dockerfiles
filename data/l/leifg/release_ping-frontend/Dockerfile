FROM node:9.3.0  
LABEL maintainer="Leif Gensert <leif@leif.io>"  
  
RUN apt-get update  
RUN apt-get -y install python2.7-minimal python2.7-dev zip unzip build-
essential git moreutils jq  
  
# Install AWS CLI  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip"  
RUN unzip awscli-bundle.zip  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN rm -rf ./awscli-bundle/  
  
# Install Elm App and yarn  
ENV YARN_VERSION=1.3.2  
RUN npm install -g yarn@${YARN_VERSION}  
RUN yarn global add create-elm-app  
  
# Install Semantic Release Go  
ENV SEMANTIC_RELEASE_VERSION=1.6.2  
ADD https://github.com/semantic-release/go-semantic-
release/releases/download/v${SEMANTIC_RELEASE_VERSION}/semantic-
release_v${SEMANTIC_RELEASE_VERSION}_linux_amd64 /usr/local/bin/semantic-
release  
RUN chmod a+x /usr/local/bin/semantic-release  

