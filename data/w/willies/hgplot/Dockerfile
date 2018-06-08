FROM python:3-alpine  
  
RUN pip install --upgrade pip  
  
RUN pip install pyyaml \  
plotly \  
paho-mqtt \  
pytz  
  
ADD hgplot.py /hgplot.py  
  
ENTRYPOINT python /hgplot.py  

