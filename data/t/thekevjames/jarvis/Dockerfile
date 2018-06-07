FROM python:3.5.2-alpine  
  
ENV PYTHONPATH=/src  
  
COPY requirements.txt /src/requirements.txt  
RUN pip install --upgrade pip && \  
pip install --no-cache-dir -r /src/requirements.txt  
  
COPY setup.py /src/setup.py  
COPY setup.cfg /src/setup.cfg  
COPY jarvis /src/jarvis  
RUN cd /usr/local/lib/python3.5/site-packages && python /src/setup.py develop  
  
COPY plugins /plugins  
  
CMD jarvis  

