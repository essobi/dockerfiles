FROM python:3.5  
ADD ./orcs /orcs  
WORKDIR /orcs  
RUN pip install --upgrade pip && pip install -r requirements.txt  
CMD make test  

