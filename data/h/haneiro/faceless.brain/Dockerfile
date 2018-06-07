FROM python:3.6  
RUN mkdir -p /var/www/app  
WORKDIR /var/www/app  
ENV PYTHONDONTWRITEBYTECODE 1  
ENV DOCKER true  
  
RUN apt-get update && \  
apt-get install -y mysql-client vim  
ADD ./requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

