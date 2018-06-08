FROM node  
  
ENV APP=/usr/src/app  
ADD . $APP  
  
WORKDIR $APP  
  
RUN (cd backend && yarn install) \  
&& (cd frontend && yarn install)  
  
EXPOSE 1337  
ENTRYPOINT "$APP/entrypoint.sh"  

