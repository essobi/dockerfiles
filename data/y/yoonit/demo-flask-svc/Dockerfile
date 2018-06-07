FROM python:3.6  
WORKDIR /app  
ENV FLASK_APP=/app/demo/main.py  
EXPOSE 8080  
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]  
COPY requirements.txt /app/requirements.txt  
COPY vendor /app/vendor  
RUN pip install -r requirements.txt  
COPY demo /app/demo  

