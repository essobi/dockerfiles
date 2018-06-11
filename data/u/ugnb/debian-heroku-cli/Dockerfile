FROM debian:jessie-slim  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common curl apt-transport-https  
RUN add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt
./"  
RUN curl -L https://cli-assets.heroku.com/apt/release.key | apt-key add -  
RUN apt-get update  
RUN apt-get install -y heroku  
RUN touch ~/.netrc  
  
CMD ["heroku", "login"]  

