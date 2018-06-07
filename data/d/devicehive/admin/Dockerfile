FROM node:8  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
RUN npm install serve -g && npm install  
  
EXPOSE 5000  
CMD REACT_APP_SERVER_URL=${REACT_APP_SERVER_URL}
REACT_APP_POLL_HISTORY_SIZE=${REACT_APP_POLL_HISTORY_SIZE} npm run build &&
serve -s build && npm cache clean --force

