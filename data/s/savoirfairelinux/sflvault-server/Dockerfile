FROM python:3-alpine3.6  
RUN apk add --no-cache \  
bash libpq gettext gcc musl-dev \  
postgresql-dev uwsgi uwsgi-python3  
  
WORKDIR /code  
COPY ./ /code/  
  
RUN pip3 install pipenv  
RUN pipenv install --system  
  
CMD /code/utils/docker-command.sh  

