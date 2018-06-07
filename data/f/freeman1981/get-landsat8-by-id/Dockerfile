FROM python:2.7  
RUN apt-get update && apt-get install -y \  
python-openssl \  
libffi-dev \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /server  
  
COPY requirements.txt requirements.txt  
  
RUN pip install -r requirements.txt  
  
ADD service_get_ls8.py service_get_ls8.py  
  
EXPOSE 8000  
CMD python service_get_ls8.py

