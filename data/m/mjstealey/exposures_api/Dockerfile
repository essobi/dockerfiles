FROM python:3  
MAINTAINER Michael J. Stealey <michael.j.stealey@gmail.com>  
  
# Set default environment variables  
# [connexion/api-server]  
ENV CONNEXION_SERVER=  
ENV CONNEXION_DEBUG=True  
ENV API_SERVER_HOST=localhost  
ENV API_SERVER_PORT=5000  
ENV API_SERVER_KEYFILE=  
ENV API_SERVER_CERTFILE=  
# [sys-path]  
ENV SYS_PATH_EXPOSURES=/exposures-api/exposures  
ENV SYS_PATH_CONTROLLERS=/exposures-api/controllers  
# [postgres]  
ENV POSTGRES_HOST=backend  
ENV POSTGRES_PORT=5432  
ENV POSTGRES_DATABASE=bdtgreen  
ENV POSTGRES_USERNAME=datatrans  
ENV POSTGRES_PASSWORD=somepassword  
ENV POSTGRES_IP=  
  
COPY . /exposures-api  
WORKDIR /exposures-api  
  
RUN pip install --upgrade pip \  
&& pip install -r requirements.txt  
  
ENTRYPOINT ["/exposures-api/docker-entrypoint.sh"]  
EXPOSE 5000  
CMD ["app.py"]

