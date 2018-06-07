##  
# NodeJS with Swagger executables  
##  
FROM node:9.11  
RUN npm install -g swagger  
  
RUN ( \  
echo "swagger project create" && \  
echo "swagger project edit -s --host 0.0.0.0 --port 3001" && \  
echo "swagger project start" && \  
echo "node --inspect-brk=0.0.0.0:3001 app.js" && \  
echo "node --inspect=0.0.0.0:3001 app.js" \  
) >> $HOME/.bash_history  
  
EXPOSE 3001  
EXPOSE 10010  
CMD [ "swagger", "project", "start" ]  

