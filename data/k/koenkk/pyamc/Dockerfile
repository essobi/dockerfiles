FROM python:3.6  
# Copy files  
RUN mkdir /app  
COPY *.py /app/  
COPY requirements.txt /app/  
  
# Install dependencies  
RUN pip install -r /app/requirements.txt  
  
RUN cd /tmp && \  
wget https://www.rarlab.com/rar/rarlinux-x64-5.5.0.tar.gz && \  
tar -zxvf rarlinux-*.tar.gz && \  
cp rar/rar /usr/local/bin && \  
cp rar/unrar /usr/local/bin  
  
RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install transmission-remote-cli ffmpeg -y && \  
apt-get clean  
  
EXPOSE 5000  
ENTRYPOINT ["python", "/app/pyamc.py"]  

