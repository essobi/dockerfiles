FROM python:3.6-alpine  
  
RUN adduser -D python  
WORKDIR /home/python  
COPY flask/requirements.txt ./  
RUN pip install -U -r requirements.txt  
COPY flask ./  
CMD FLASK_APP=main.py flask run -p 80 -h 0.0.0.0  

