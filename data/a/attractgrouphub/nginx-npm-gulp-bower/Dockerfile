FROM nginx:stable  
  
MAINTAINER AttractGroup  
  
RUN apt-get update && apt-get install -y curl wget git net-tools vim less
screen gnupg gnupg2 apt-transport-https  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
RUN apt-get install -y nodejs  
  
RUN npm install -g bower && npm install -g gulp  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

