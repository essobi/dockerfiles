FROM maguowei/base  
MAINTAINER imaguowei@gmail.com  
  
WORKDIR /stark/stark  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libjpeg-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./requirements.txt ./  
RUN pip3 install --no-cache-dir -r requirements.txt  
  
EXPOSE 8000  

