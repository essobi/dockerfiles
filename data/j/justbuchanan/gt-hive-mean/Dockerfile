FROM justbuchanan/docker-archlinux  
  
RUN pacman -Sy --noconfirm nodejs npm git  
RUN npm install -g -y nodemon bower gulp  
  
COPY ./ gthive  
WORKDIR gthive  
  
RUN npm install  
RUN bower install --allow-root  
  
EXPOSE 8080  
CMD ["gulp"]  

