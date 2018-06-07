FROM groonga/rroonga:latest  
  
# Poppler  
RUN apt-get install -y poppler-utils fonts-ipaexfont-gothic  
  
# Honyomi  
RUN gem install honyomi -v 1.5 --no-ri --no-rdoc  
RUN honyomi init  
  
EXPOSE 9295  
CMD honyomi web --host=0.0.0.0 --no-browser  

