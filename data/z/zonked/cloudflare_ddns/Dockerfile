FROM python:3  
ADD requirements.txt update_ddns.py /app/  
WORKDIR /app  
RUN pip3 install -r requirements.txt  
ENTRYPOINT ["python3", "-u", "/app/update_ddns.py"]

