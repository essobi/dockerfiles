FROM python:3.6.1-alpine  
COPY requirements.txt /  
RUN pip install --no-cache-dir -r requirements.txt  
CMD ["ofxstatement", "convert", "-t","swedbankLV"]  

