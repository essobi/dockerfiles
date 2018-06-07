FROM nginx:1.9  
MAINTAINER James Badger <james@jamesbadger.ca>  
  
ADD ./preconfigure.sh /preconfigure.sh  
COPY dist /usr/share/nginx/html  
  
CMD ./preconfigure.sh  

