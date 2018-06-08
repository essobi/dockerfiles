FROM python:2.7  
MAINTAINER Praekelt Foundation <dev@praekeltfoundation.org>  
RUN apt-get update  
RUN apt-get install -qy redis-server  
RUN apt-get autoremove -qy  
RUN pip install gunicorn  
RUN pip install supervisor  
ENV GARELAY_VERSION 0.2.0  
RUN pip install garelay==$GARELAY_VERSION  
ENV GARELAY_PORT 8000  
ENV GARELAY_SERVER http://www.example.com/server/  
ENV GARELAY_ROOT=/garelay  
ENV DATABASE_URL sqlite:///$GARELAY_ROOT/db.sqlite3  
COPY ./docker-entrypoint.sh /  
EXPOSE $GARELAY_PORT  
VOLUME $GARELAY_ROOT  
ENTRYPOINT ["./docker-entrypoint.sh"]  

