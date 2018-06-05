FROM fernandoe/docker-python:0.0.4  
MAINTAINER Fernando Espíndola <fer.esp@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
libpq-dev \  
&& apt-get -y autoremove && apt-get -y autoclean && apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD ./requirements.txt /requirements.txt  
ADD ./source /app  
  
RUN pip install -r /requirements.txt  
  
WORKDIR /app  
  
CMD ["python", "application.py"]  

