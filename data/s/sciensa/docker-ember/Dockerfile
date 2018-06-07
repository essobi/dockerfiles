FROM node:8  
  
WORKDIR /home/apps  
  
RUN mkdir -p /home/apps/build/dist  
  
# update packege  
RUN apt-get update -y && apt-get install -y git nginx  
  
# install bower  
RUN npm install -g bower  
  
# install ember  
RUN npm install -g ember-cli@2.15.0  
  
# Copy ember.conf to default nginx conf  
RUN rm /etc/nginx/sites-enabled/default  
COPY ember.conf /etc/nginx/sites-enabled/default  
  
# move entrypoint  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
  
# give permission to execute sh  
RUN chmod +x /usr/bin/entrypoint.sh  
  
# expose port 80  
EXPOSE 80  
  
# entrypoint  
ENTRYPOINT ["su", "-c", "/usr/bin/entrypoint.sh"]

