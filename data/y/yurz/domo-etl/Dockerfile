FROM yurz/pybase  
  
LABEL authors="Yuri Zhylyuk yuri@zhylyuk.com"  
  
RUN \  
apt-get -y update && \  
apt-get -y install git && \  
pip install --upgrade pip && \  
pip install git+https://github.com/domoinc/domo-python-sdk.git && \  
rm -rf /var/lib/{cache,log}/ && \  
mkdir /app  
WORKDIR /app  
CMD ["python", "./app.py"]

