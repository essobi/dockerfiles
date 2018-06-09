FROM node:6  
WORKDIR /opt/demo  
  
RUN npm install -g trambar-deco  
  
RUN git clone \--depth 1 https://github.com/chung-leong/trambar.git  
  
CMD cd trambar/client && trambar-deco --no-watch --no-shutdown --port 80  

