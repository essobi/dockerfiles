FROM python:3.4  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
RUN pip install Flask==0.10.1 uWSGI==2.0.8 requests==2.5.1 redis==2.10.3  
WORKDIR /app  
COPY ./cmd.sh /  
RUN chmod +x /cmd.sh  
COPY ./app /app  
EXPOSE 9090 9191  
USER uwsgi  
CMD ["/cmd.sh"]  

