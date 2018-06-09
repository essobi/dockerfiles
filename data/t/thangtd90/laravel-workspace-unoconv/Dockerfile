FROM framgia/laravel-workspace  
  
RUN apt-get update && apt-get install -y --force-yes unoconv php7.1-soap  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

