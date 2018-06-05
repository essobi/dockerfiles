FROM python:2  
ADD requirements.txt /app/requirements.txt  
WORKDIR /app  
RUN pip install -r requirements.txt  
ADD . /app  
  
ENV FLASK_APP api.py  
EXPOSE 5000  
ENTRYPOINT ["python", "-m", "flask", "run"]  
CMD ["-h", "0.0.0.0", "-p", "5000"]  

