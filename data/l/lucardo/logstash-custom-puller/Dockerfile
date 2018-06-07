FROM python  
  
RUN pip install --upgrade pip && pip install decorator  
  
COPY puller.py /  
  
ENV SRV_ENCODE latin_1  
  
CMD ["python", "-u", "/puller.py"]

