FROM python:2  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
mysql-client libc-ares2 libssl1.0.0 libcrypto++9 libsodium13 libfreeimage3 \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
COPY requirements.txt ./  
COPY "megasdk-3.2.6-py2.py3-none-any.whl" ./  
RUN pip install -r requirements.txt && ldconfig /usr/local/lib/python2.7/site-
packages/mega/  
COPY . .  
# Need to add migration  
EXPOSE 8000  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  

