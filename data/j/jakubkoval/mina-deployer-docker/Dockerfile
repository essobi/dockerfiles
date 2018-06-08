FROM ruby:alpine  
RUN gem install mina && gem install mina-multistage  
  
ENV SSH_AUTH_SOCK /root/ssh-agent  
  
WORKDIR /root/workdir  
  
ENTRYPOINT ["mina"]

