FROM python:3.4-slim  
  
MAINTAINER Akshaya Acharya <akshaya@34cross.in>  
  
RUN pip install --upgrade oauth2client  
  
COPY update_docker_credentials.py generate_token.py dict_merge.py /token/  
  
RUN chmod +x /token/update_docker_credentials.py  
  
ENTRYPOINT ["/token/update_docker_credentials.py"]  

