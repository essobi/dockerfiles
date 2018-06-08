FROM alpine:3.6  
WORKDIR /app  
  
COPY requirements.txt requirements.txt  
  
RUN apk add --update --no-cache \  
python3 \  
&& pip3 install -r requirements.txt  
  
COPY . /app  
  
ENTRYPOINT ["/usr/bin/env", "python3", "plex_data_collector.py"]  

