FROM python:3.6-slim  
  
RUN pip install pipenv &&\  
apt-get update &&\  
apt-get install -y doxygen  
  
WORKDIR /usr/src  
VOLUME /usr/src/data  
  
COPY Pipfile* ./  
RUN pipenv install --system  
  
COPY doxy-my-docs.py .  
COPY doxymydocs ./doxymydocs  
  
ENTRYPOINT [ "python", "doxy-my-docs.py" ]  

