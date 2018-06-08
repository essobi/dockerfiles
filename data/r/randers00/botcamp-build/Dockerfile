FROM randers00/openjdk-gradle:4.1  
LABEL maintainer="Ruben Anders <rubenanders@outlook.de>"  
  
RUN wget -q -O - https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
RUN npm install gitbook-cli -g  
RUN gitbook fetch latest  

