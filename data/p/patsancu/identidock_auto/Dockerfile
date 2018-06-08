FROM python:3.4  
  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
RUN pip install Flask==0.10.1 uWSGI==2.0.8  
  
EXPOSE 9090 9191 5000  
USER uwsgi  
COPY app /app  
COPY cmd.sh /  
CMD ["/cmd.sh"]  

