FROM python:3.6  
ENV APP_HOME /otodom-crawler  
  
WORKDIR $APP_HOME  
  
ADD requirements.txt $APP_HOME/  
RUN pip install -r requirements.txt  
  
ADD . $APP_HOME  

