# Latest stable  
FROM debian:stretch  
  
RUN apt-get update && apt-get install -y \  
python3 \  
python3-pip \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
ADD requirements.txt /app/requirements.txt  
  
RUN pip3 install -r /app/requirements.txt  
  
ADD . /app  
WORKDIR /app  
  
ENTRYPOINT ["python3", "/app/anonymize.py", "--no-log"]  

