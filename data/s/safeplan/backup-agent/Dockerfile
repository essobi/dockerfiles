FROM python:3  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
libssl-dev \  
openssl \  
libacl1-dev \  
libacl1 \  
build-essential \  
libfuse-dev \  
fuse \  
pkg-config \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install --no-cache-dir borgbackup==1.1.5 llfuse  
  
VOLUME ["/var/safeplan/backup" , "/var/safeplan/config", "/var/safeplan/repo",
"/var/safeplan/work", "/root/.ssh" , "/var/safeplan/history"]  
  
ENV SAFEPLAN_ID NOT_SET  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
  
RUN pip3 install --no-cache-dir -r requirements.txt  
  
COPY api /usr/src/app  
  
EXPOSE 8080  
ENV TZ=Europe/Vienna  
  
ENTRYPOINT ["python3"]  
  
CMD ["app.py"]

