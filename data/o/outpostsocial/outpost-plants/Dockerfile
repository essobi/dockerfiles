FROM python:3.6  
RUN mkdir /app  
WORKDIR /app  
COPY . /app  
RUN pip install -r requirements.txt  
EXPOSE 5000  
# Start gunicorn  
CMD ["gunicorn", "server:app"]

