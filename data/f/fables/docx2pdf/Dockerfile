FROM python:3.6.2-jessie  
  
RUN echo deb http://ftp.ru.debian.org/debian/ jessie main non-free contrib >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \  
libreoffice-writer \  
openjdk-7-jre-headless \  
ttf-mscorefonts-installer \  
&& pip install aiohttp \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD ./proxy /proxy/  
  
ENV PORT 6000  
  
CMD ["python", "/proxy/main.py"]

