FROM python:2.7-alpine  
MAINTAINER Ravishankar Sivasubramaniam "ravi_siva@live.com"  
RUN addgroup -S flaskuser && adduser -S -g flaskuser flaskuser  
  
#ADD . /flaskapp  
ENV HOME /flaskapp  
ENV PATH $PATH:/flaskapp  
  
  
WORKDIR /flaskapp  
COPY requirements.txt /flaskapp/  
COPY manage.py /flaskapp/  
COPY runserver.sh /flaskapp/  
  
RUN pip install gunicorn  
RUN pip install -r requirements.txt  
  
COPY flaskapp /flaskapp/flaskapp  
COPY runserver.sh /usr/local/bin/  
  
RUN chmod 755 /flaskapp/runserver.sh  
RUN chmod 755 /usr/local/bin/runserver.sh  
  
RUN echo "Listing"  
RUN ls -ltr /flaskapp  
RUN ls -ltr /flaskapp/flaskapp  
  
RUN pwd  
#RUN python manage.py db init  
#RUN python manage.py db migrate  
#RUN python manage.py db upgrade  
EXPOSE 4000  
CMD ["runserver.sh"]  
#ENTRYPOINT ["python"]  
#CMD ["manage.py","runserver"]  

