# https-redirect  
  
FROM node:0.10  
MAINTAINER Joey Baker <joey@getable.com>  
  
# Install upgrade node and npm  
RUN npm install -g nave \  
&& nave usemain stable \  
&& npm i -g npm \  
&& npm rm -g nave \  
# install https-redirect  
&& npm i -g https-redirect@1.0.0  
  
EXPOSE 80  
  
CMD ["https-redirect", "-p 80", "-1"]  
  

