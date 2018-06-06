FROM node:6  
  
ENV HOME=/var/www  
WORKDIR $HOME/client  
  
COPY . .  
  
# RUN apk update  
# RUN apk add --update alpine-sdk  
RUN yarn global add @angular/cli@latest  
RUN ng set \--global packageManager=yarn  
RUN yarn  
# RUN apk del alpine-sdk  
# RUN rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm  
RUN npm cache clear  
RUN sed -i -e "s/bin\/ash/bin\/sh/" /etc/passwd  

