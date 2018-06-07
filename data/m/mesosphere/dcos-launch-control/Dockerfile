FROM python:3.5-slim  
COPY . /cloudcleaner  
WORKDIR /cloudcleaner  
RUN apt-get update && \  
apt-get install -y git libffi-dev && \  
rm -rf /var/lib/apt/lists/*  
RUN pip3 install -r requirements.txt && \  
python3 setup.py develop  
CMD ["cloudcleaner", "--help"]  

