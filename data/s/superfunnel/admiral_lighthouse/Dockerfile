FROM python:3.6  
WORKDIR /app  
ENV PYTHONPATH /app  
EXPOSE 1988  
COPY requirements.txt /app/  
COPY app.py /app/  
RUN pip install -r requirements.txt  
HEALTHCHECK \--interval=30s --timeout=10s \  
CMD curl -f http://0.0.0.0:1988/stat || exit 1  
ENTRYPOINT ["python", "./app.py"]  

