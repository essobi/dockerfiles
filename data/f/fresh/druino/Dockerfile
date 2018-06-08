FROM rubinius/docker:latest  
  
RUN gem install druino -V  
RUN apt-get update  
RUN apt-get install -y avrdude  
  
CMD rbx -r druino  
  

