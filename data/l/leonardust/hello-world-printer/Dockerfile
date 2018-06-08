FROM python:2.7  
WORKDIR /tmp  
ADD requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
RUN mkdir -p /usr/src/hello_world_printer/  
ADD hello_world/ /usr/src/hello_world_printer/hello_world/  
  
ADD main.py /usr/src/hello_world_printer/  
RUN ls /usr/src/hello_world_printer  
  
CMD PYTHONPATH=$PYTHONPATH:/usr/src/hello_world_printer \  
FLASK_APP=hello_world flask run --host=0.0.0.0

