# Dockerfile for models  
FROM ubuntu:17.10  
ENV FLASK_PROXY_PORT 8080  
RUN apt-get update \  
&& apt-get install -y software-properties-common curl \  
&& apt-get install -y python2.7-dev \  
&& curl -o /tmp/get-pip.py "https://bootstrap.pypa.io/get-pip.py" \  
&& python2.7 /tmp/get-pip.py \  
&& apt-get remove -y curl \  
&& apt autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# Upgrade and install basic Python dependencies  
RUN apt-get clean autoclean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
RUN mkdir -p /actionProxy  
  
ADD actionproxy.py /actionProxy/  
  
RUN mkdir -p /action  
  
RUN apt-get update && apt-get install -y \  
libopencv-dev wget unzip cmake make opencv-data  
  
ADD requirements.txt requirements.txt  
  
RUN python2.7 -m pip install --default-timeout 100 -r requirements.txt  
RUN python2.7 -m textblob.download_corpora  
RUN python2.7 -m nltk.downloader stopwords  
  
### archivos de modelos  
ADD modelrf10h.pkl /action/  
ADD exec /action/  
RUN chmod +x /action/exec  
  
CMD ["/bin/bash", "-c", "cd actionProxy && python2.7 -u actionproxy.py"]  

