FROM python:3.6.3  
RUN mkdir -p /app  
COPY ./worker /app/worker  
COPY ./Pipfile /tmp  
COPY ./Pipfile.lock /tmp  
  
RUN ln -s /usr/local/bin/python /bin/python # Without this line, pipenv don't
work  
RUN pip3 install pipenv  
  
RUN cd /tmp && pipenv install --system  
  
WORKDIR /app  
CMD ["rqworker", "-c", "worker.settings"]

