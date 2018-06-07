FROM mhart/alpine-node  
  
COPY app/ /opt/  
  
WORKDIR /opt/  
  
RUN npm install  
  
# EXPOSE PORTS  
EXPOSE 80  
CMD ["node", "index.js"]  

