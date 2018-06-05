FROM python:3.6-slim  
WORKDIR /app  
ADD . /app  
RUN pip install -r requirements.txt  
EXPOSE 80  
ENV DB_CONNECTION_STRING mongodb://mongo:27017  
ENV SECRET_KEY super-secret  
ENV DEBUG True  
CMD ["python", "app.py"]  

