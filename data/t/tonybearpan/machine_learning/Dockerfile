FROM python:3.5  
COPY requirements.txt /requirements.txt  
COPY start.sh /start.sh  
  
RUN pip install -r requirements.txt  
  
EXPOSE 5000  
CMD ["sh", "start.sh"]

