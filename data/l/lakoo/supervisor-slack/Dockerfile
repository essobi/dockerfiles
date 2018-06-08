FROM lakoo/python:2.7-slim  
RUN mkdir /supervisor-slack  
WORKDIR /supervisor-slack  
COPY requirements.txt /supervisor-slack/  
RUN pip install -r requirements.txt  
COPY . /supervisor-slack  
CMD [ "supervisord", "-n", "-c", "conf/supervisord.conf" ]  

