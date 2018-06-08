FROM gallna/grunt  
MAINTAINER Tomasz Jonik <tomasz@hurricane.works>  
  
# Install Grunt watch, devtools and livereload  
RUN npm install -g grunt-devtools grunt-livereload  
  
# Define working directory.  
WORKDIR /data  
  
# Expose Devtools extension  
EXPOSE 61750  
# Expose Livereload extension  
EXPOSE 35729  
# Define default command.  
CMD ["grunt-devtools"]  

