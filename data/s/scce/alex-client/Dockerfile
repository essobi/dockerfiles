FROM debian:stable as cloner  
RUN apt-get update && \  
apt-get install -y git  
RUN git clone https://github.com/LearnLib/alex.git --branch developer
--single-branch  
  
FROM node:9.2.1  
WORKDIR /alex-cli  
COPY \--from=cloner /alex/cli/src/main/javascript .  
RUN npm install -g  
ENTRYPOINT ["/usr/local/bin/alex-cli"]  
CMD ["--help"]  

