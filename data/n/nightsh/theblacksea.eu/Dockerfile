FROM python:3.6  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY requirements.txt /app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
ENV PYTHONUNBUFFERED 1  
ENV PYTHONDONTWRITEBYTECODE 1  
ENV LANG en_US.UTF-8  
ENV PYTHONIOENCODING utf_8  

