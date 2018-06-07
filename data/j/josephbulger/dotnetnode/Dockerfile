FROM microsoft/dotnet  
  
RUN apt-get update && apt-get install -y -q --no-install-recommends  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 6.5.0  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  

