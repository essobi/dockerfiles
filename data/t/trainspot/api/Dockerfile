FROM python:3-alpine  
  
ENV APP_PATH /api  
  
RUN apk add python-dev mariadb-dev gcc musl-dev linux-headers --update-cache  
  
WORKDIR ${APP_PATH}  
  
COPY requirements.txt ./  
RUN pip install -r requirements.txt  
  
COPY company/ ./company/  
COPY equipment/ ./equipment/  
COPY media/ ./media/  
COPY search/ ./search/  
COPY shay/ ./shay/  
COPY spot/ ./spot/  
COPY tspt/ ./tspt/  
COPY manage.py uwsgi.ini run.sh ./  
  
RUN mkdir static  
RUN chmod 755 run.sh  
  
RUN chown -R 1057860000:1057860000 ${APP_PATH}  
  
# uWSGI will listen on this port  
EXPOSE 8000  
ENTRYPOINT ["./run.sh"]  

