#########################################################################  
#  
# Codeception container - used by our PHP applications  
#  
# Build with:  
# docker build -t="tuyakhov/codeception" .  
#  
#  
########################################################################  
  
FROM tuyakhov/stombox-php  
  
# Install codeception and make it executable  
ADD http://codeception.com/codecept.phar /usr/local/bin/codecept  
RUN chmod +x /usr/local/bin/codecept  
  
# Make codecept the default command  
ENTRYPOINT ["codecept"]  
  
WORKDIR /tests  

