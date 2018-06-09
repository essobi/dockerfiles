FROM tiangolo/uwsgi-nginx-flask:python3.6  
COPY ./ctms-rest-api ./requirements.txt ./docker/setup.sh /app/  
RUN bash /app/setup.sh  
COPY ./docker/uwsgi.ini /app/uwsgi.ini  

