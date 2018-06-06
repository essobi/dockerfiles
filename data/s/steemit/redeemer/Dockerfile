FROM python:3.6  
RUN touch /var/log/messages  
  
RUN pip install pipenv  
  
WORKDIR /usr/src/app  
ADD Pipfile Pipfile.lock ./  
RUN pipenv install  
ADD . .  
  
ENTRYPOINT [ "pipenv", "run", "./delegate.py" ]  

