FROM python:3.4  
  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
RUN pip install Flask==0.10.1 uWSGI==2.0.8 requests==2.5.1 redis==2.10.3  
WORKDIR /app  
COPY app $WORKDIR  
COPY cmd.sh /  
  
# Expose port to other containers. If you do not expose and use publish (-p or
-P) docker  
# does an implicit EXPOSE.  
EXPOSE 9090 9191  
  
# Set the user for all the following lines (including CMD and ENTRYPOINT)  
USER uwsgi  
  
CMD ["/cmd.sh"]  

