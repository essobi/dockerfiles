FROM logicify/python3  
MAINTAINER "Dmitry Berezovsky <dmitry.berezovsky@logicify.com>"  
ENV APP_PROCESS_NAME="wsgi-application"  
ENV APP_MODULE="wsgi"  
ENV APP_WORKERS_COUNT="4"  
ENV TIMEOUT="30"  
ENV APP_LOG_LEVEL="info"  
ENV APP_PORT="8000"  
ENV APPLICATION_DIR="/srv/application"  
RUN source /srv/virtenv/bin/activate && pip install gunicorn==19.6.0  
  
EXPOSE $APP_PORT  
ADD start-gunicorn.sh /home/app/start-gunicorn.sh  
  
CMD /home/app/start-gunicorn.sh  

