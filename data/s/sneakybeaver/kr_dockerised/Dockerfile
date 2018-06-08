FROM python  
  
WORKDIR /opt/kr_app  
  
COPY requirements.txt ./  
  
COPY config.py ./  
  
RUN pip install --no-cache-dir -r requirements.txt  
  
CMD ["knowledge_repo","runserver","--config","config.py"]

