FROM google/nodejs  
  
#PhantomJS dependencies  
RUN apt-get update && apt-get install -y libfreetype6 libfontconfig && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install -g bower grunt-cli

