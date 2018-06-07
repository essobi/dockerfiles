FROM nginx  
  
LABEL license="Apache License, Version 2.0"  
LABEL copyright="CS Systèmes d'Information"  
LABEL maintainer="contact@ikats.org"  
LABEL version="0.7.39"  
  
MAINTAINER Germain GAU <germain.gau@c-s.fr>  
  
RUN rm -rf /usr/share/nginx/html  
  
ADD container_init.sh /  
ADD src /usr/share/nginx/html  
  
CMD ["bash", "/container_init.sh"]  

