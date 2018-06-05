FROM python:2.7-onbuild  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
build-essential \  
cmake \  
python3-gi \  
gir1.2-webkit-3.0  
  
CMD [ "python", "./brick-browser.py" ]  

