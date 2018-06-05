FROM ruby:2.3  
RUN gem install apiaryio  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g api-blueprint-validator-module@1.2.2 markdown-styles@3.1.9  
ENTRYPOINT ["/bin/bash"]  

