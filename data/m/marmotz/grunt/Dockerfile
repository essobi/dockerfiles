FROM marmotz/nodejs  
  
USER root  
  
# Install Bower & Grunt  
RUN npm install -g bower grunt grunt-cli  
  
# Install compass  
RUN apt-get update -y && apt-get install -y ruby ruby-dev build-essential && \  
gem install compass  
  
ADD init_grunt.sh /  
  
USER nonrootuser  
  
CMD ["/init_grunt.sh"]  

