# Extend from current stable php apache  
FROM prefernz/php:7.2  
# OS packages  
RUN apt-get -y update && apt-get install -y \  
gnupg \  
build-essential  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install --no-install-recommends -y \  
nodejs  
  
# Update npm  
RUN npm install -g npm  
  
# Cleanup  
RUN rm -r /var/lib/apt/lists/*  

