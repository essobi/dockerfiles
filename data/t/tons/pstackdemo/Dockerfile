FROM python:3.4-alpine  
WORKDIR /src  
ADD . /src  
RUN pip install -r requirements.txt  
CMD python app.py  
HEALTHCHECK \--interval=1m --timeout=3s \  
CMD wget -q -O - http://localhost:8000/ || exit 1  

