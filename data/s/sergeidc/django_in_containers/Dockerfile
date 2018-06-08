FROM python:3.4  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /dj_app  
WORKDIR /dj_app  
ADD ./dj_app/requirements.txt /dj_app/  
RUN pip install -r requirements.txt  
EXPOSE 8000 9191  
COPY ./dj_app/docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
#ENTRYPOINT ["uwsgi", "--wsgi-file", "dj_main/wsgi.py", "--memory-report", "--
master", "--processes", "2", "--threads", "1"]  
CMD ["--socket", ":8000", "--stats", ":9191"]

