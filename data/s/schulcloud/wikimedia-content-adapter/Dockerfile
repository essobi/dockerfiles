  
FROM node:6.11.0  
# install wikimedia-content-adapter  
RUN useradd --system --user-group --create-home app && \  
mkdir /app && chown app:app /app  
COPY package.json /opt/  
RUN cd /opt && npm install  
ENV NODE_PATH=/opt/node_modules  
  
COPY . /app  
  
USER app  
WORKDIR /app  
  
# bind on port 3000  
EXPOSE 3000  
CMD ["node", "app.js"]  

