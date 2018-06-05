FROM python:2.7.13  
  
RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.py |
python -c "import sys; main=lambda:sys.stderr.write('Download failed\n');
exec(sys.stdin.read()); main()"  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
fonts-arphic-ukai \  
fonts-arphic-uming &&\  
rm -rf /var/lib/apt/lists/*

