FROM grmanit/jenkins-nodejs  
  
RUN apt-get update && apt-get install -y ruby-full && rm -rf
/var/lib/apt/lists/* &&\  
gem install bundler  
  
RUN chmod -R 777 /var/lib/gems /usr/local  

