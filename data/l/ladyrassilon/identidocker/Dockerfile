FROM python:3.6  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
RUN pip install Flask==0.12  
RUN pip install uWSGI==2.0.14  
RUN pip install requests==2.13.0  
RUN pip install redis==2.10.5  
WORKDIR /app  
COPY app /app  
COPY cmd.sh /  
  
EXPOSE 9090 9191  
USER uwsgi  
  
CMD ["/cmd.sh"]  

