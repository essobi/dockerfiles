FROM python:3.6  
WORKDIR /app  
ADD . /app  
RUN pip install -r requirements.txt  
EXPOSE 5001  
ENV NAME test-site  
CMD ["python","run.py"]  

