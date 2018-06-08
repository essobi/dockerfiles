FROM ubuntu  
  
RUN apt-get update && apt-get -y install git build-essential curl && apt-get
clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g yarn gulp  

