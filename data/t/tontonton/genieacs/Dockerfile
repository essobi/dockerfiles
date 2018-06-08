FROM starefossen/ruby-node:2-8  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install mongodb -y  
RUN service mongodb start  
  
ENV APP_HOME /app/genieacs  
RUN mkdir $APP_HOME -p  
WORKDIR $APP_HOME  
RUN npm install genieacs  
  
Add . $APP_HOME  
  
EXPOSE 7557  
CMD ["./start.sh"]  

