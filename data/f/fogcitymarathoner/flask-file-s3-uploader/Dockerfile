FROM fogcitymarathoner/dockerfile-php5.6.22-python2.7.11  
ENV PYTHONUNBUFFERED 1  
ENV TERM=xterm  
EXPOSE 9191-9200  
RUN apt-get update  
  
# install flask  
RUN pip install --upgrade pip  
ADD requirements.txt .  
RUN /usr/local/bin/pip install -r ./requirements.txt  
ADD app.py .  
ADD config ./config/  
ADD server_config ./server_config/  
ADD data ./data/  
ADD lib ./lib/  
ADD static ./static/  
ADD templates ./templates/  
# entrypoint for ECS to run  
ADD docker-entrypoint.sh .  
RUN chmod 755 ./docker-entrypoint.sh  
  
# check python version  
RUN which python  
RUN python --version  
RUN pip freeze  
  

