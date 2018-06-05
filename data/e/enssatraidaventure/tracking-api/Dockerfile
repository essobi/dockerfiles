FROM python:2.7  
# Install app dependencies  
COPY requirements.txt /src/requirements.txt  
RUN cd /src; pip install -r requirements.txt  
  
# Bundle app source  
COPY ./src /src  
  
EXPOSE 8081  
CMD /bin/sh -c 'cd /src; python server.py'  

