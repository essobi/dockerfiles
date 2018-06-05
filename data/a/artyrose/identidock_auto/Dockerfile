FROM python:3.4  
  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
RUN pip install Flask==0.10.1 uWSGI==2.0.8 requests==2.5.1  
RUN pip install redis==2.10.3  
COPY cmd.sh /cmd.sh  
WORKDIR /app  
COPY app /app  
  
EXPOSE 9090 9191  
USER uwsgi  
  
# CMD ["--http", "0.0.0.0:9090", "--wsgi-file", "/app/identidock.py", "--
callable", "app", "--stats", "0.0.0.0:9191"]  
ENTRYPOINT ["/cmd.sh"]  
# CMD ["/app/cmd.sh"]  

