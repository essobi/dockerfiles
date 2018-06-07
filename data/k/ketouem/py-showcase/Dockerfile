FROM python:2  
ENV APP_PATH /app/  
  
ADD . ${APP_PATH}  
RUN pip install -r ${APP_PATH}/requirements/deploy.txt  
  
WORKDIR ${APP_PATH}  

