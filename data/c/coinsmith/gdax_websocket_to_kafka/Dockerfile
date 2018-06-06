FROM python:3.6.2-stretch  
  
WORKDIR /app  
  
COPY requirements.txt ./  
RUN echo deb http://ftp.debian.org/debian stretch-backports main >>
/etc/apt/sources.list  
RUN apt-get update && apt-get -t stretch-backports install -y librdkafka1
librdkafka-dev  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . .  

