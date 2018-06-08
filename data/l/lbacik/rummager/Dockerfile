FROM python:3  
ENV RUMMAGER_LOGDIR=logs  
  
RUN mkdir -p /project/logs  
COPY . /project  
WORKDIR /project  
  
RUN pip install -r requirements.txt  
  
CMD ["python3", "rummager.py"]  

