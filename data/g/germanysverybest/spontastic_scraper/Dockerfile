FROM python:3  
WORKDIR /usr/src/app  
  
#VOLUME . /usr/src/app  
COPY . .  
  
COPY requirements.txt ./  
RUN pip3 install --no-cache-dir -r requirements.txt  
  
ENV HTTP_PROXY http://proxyserv:8118  
ENV HTTPS_PROXY http://proxyserv:8118  
ENV SOCKS_PROXY http://proxyserv:9050  
EXPOSE 80  
CMD ["python", "./app.py"]

