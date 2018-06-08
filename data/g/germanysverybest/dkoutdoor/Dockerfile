FROM python:3  
WORKDIR /usr/src/app  
  
COPY . .  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
ENV FLASK_DEBUG 1  
ENV SQLALCHEMY_DATABASE_URI
mysql://root:,mdDBani.@192.168.99.100:3306/daoutdoor?charset=utf8mb4  
  
EXPOSE 80  
CMD ["python", "./src/app.py"]

