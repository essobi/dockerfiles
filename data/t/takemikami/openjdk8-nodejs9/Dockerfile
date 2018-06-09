FROM debian:9  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jdk  
RUN apt-get install -y curl gnupg \  
&& curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get install -y nodejs \  
&& curl -L https://www.npmjs.com/install.sh | sh \  
&& npm install -g yarn  
RUN chsh -s /bin/bash  

