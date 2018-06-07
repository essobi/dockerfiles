FROM node:4.3.2  
RUN useradd --user-group --create-home --shell /bin/false frontend  
  
ENV HOME=/home/frontend/  
  
COPY ./frontend/package.json $HOME/project/package.json  
RUN chown -R frontend:frontend $HOME/*  
  
USER frontend  
WORKDIR $HOME/project  
RUN npm install  
  
USER root  
COPY ./frontend $HOME/project  
COPY ./shared-data $HOME/shared-data  
  
RUN chown -R frontend:frontend $HOME/*  
  
USER frontend  
  
RUN npm run build  
  
CMD ["npm", "start"]

