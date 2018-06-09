# DOCKER-VERSION 1.0.0  
FROM strider/strider-docker-slave  
  
USER root  
RUN apt-get install -y ruby  
USER strider  
  
ENV PATH $PATH:/home/strider/.gem/ruby/1.9.1/bin  
RUN gem install --user-install bundler  
  

