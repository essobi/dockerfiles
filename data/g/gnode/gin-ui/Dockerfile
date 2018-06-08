FROM node  
  
RUN /bin/bash  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends apache2  
  
RUN mkdir -p /gin-ui  
COPY ./ /gin-ui  
WORKDIR /gin-ui  
# The configuration file lies here (config.json)  
VOLUME /gin-ui/src/js/  
# The folder where the final app will end up in  
VOLUME /gin-ui/build  
  
RUN npm install  
  
EXPOSE 80  
ADD ./UiApacheSite.conf /etc/apache2/sites-available/000-default.conf  
  
ENTRYPOINT npm run build && a2enmod rewrite && /etc/init.d/apache2 start &&
/bin/bash  

