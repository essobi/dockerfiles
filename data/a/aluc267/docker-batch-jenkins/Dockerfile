FROM jenkinsci/blueocean:1.4.2  
USER root  
  
RUN apk update  
RUN apk add python3 jq cargo nodejs  
  
RUN pip3 install awscli rainbow  
RUN curl -o /usr/local/bin/ecs https://s3.amazonaws.com/amazon-ecs-cli/ecs-
cli-linux-amd64-latest  
RUN chmod +x /usr/local/bin/ecs  
  
RUN cargo install ripgrep  
RUN mv /root/.cargo/bin/rg /usr/local/bin/  
RUN chmod +x /usr/local/bin/rg  
RUN rm -rf /root/.cargo  
  
USER jenkins  
  
# /var/jenkins_home is defined as volume  

