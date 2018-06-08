FROM alpine:3.6  
RUN apk add --update python py-pip  
COPY requirements.txt /src/requirements.txt  
RUN pip install -U pip setuptools wheel  
RUN pip install -r /src/requirements.txt  
COPY app.py /src  
COPY engines /src/engines  
COPY docker-compose.yml /src  
CMD python /src/app.py  

