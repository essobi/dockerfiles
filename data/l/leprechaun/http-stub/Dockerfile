FROM python:3.5-alpine  
RUN pip install flask  
ADD server.py /code/server.py  
ENV FLASK_APP=server.py  
VOLUME /code  
WORKDIR /code/  
CMD flask run --host=0.0.0.0 --port=80  

