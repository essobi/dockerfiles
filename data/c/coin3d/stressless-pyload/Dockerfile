FROM debian:latest  
MAINTAINER Philipp Periventas <pp@eigenerschreckt.de>  
  
RUN sed -i 's/main/main contrib non-free/' /etc/apt/sources.list  
RUN apt-get -q update && apt-get -qy install python-crypto python-pycurl
python-imaging python-beaker python-openssl tesseract-ocr tesseract-ocr-eng
gocr unrar openssl rhino libnspr4 git  
  
RUN useradd -m -s /bin/false pyload  
WORKDIR /home/pyload/  
RUN git clone https://github.com/pyload/pyload.git  
COPY pyload-config /home/pyload/.pyload  
RUN chown -R pyload:pyload /home/pyload/.pyload  
USER pyload  
WORKDIR /home/pyload/.pyload  
RUN openssl genrsa 1024 > ssl.key && openssl req -new -key ssl.key -out
ssl.csr -subj "/C=UK/ST=Warwickshire/L=Leamington/O=OrgName/OU=IT
Department/CN=example.com" && openssl req -days 36500 -x509 -key ssl.key -in
ssl.csr > ssl.crt  
  
VOLUME ["/home/pyload/downloads/", "/home/pyload/.pyload/"]  
EXPOSE 8000  
ENTRYPOINT ["/usr/bin/python", "/home/pyload/pyload/pyLoadCore.py"]  

