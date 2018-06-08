FROM openjdk:8-jdk  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update && apt-get install -y rubygems nodejs awscli  
RUN apt-get install -y npm  
RUN gem install asciidoctor  
RUN npm install -g swagger-cli

