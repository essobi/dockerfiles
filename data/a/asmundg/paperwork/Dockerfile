from debian:jessie  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
g++ \  
gfortran \  
gir1.2-gtk-3.0 \  
gir1.2-poppler-0.18 \  
libatlas-dev \  
libblas-dev \  
libenchant-dev \  
libfreetype6-dev \  
libjpeg-dev \  
liblapack-dev \  
libpng12-dev \  
libsane \  
python-dev \  
python-gi-cairo \  
python-gobject \  
python-pip \  
tesseract-ocr \  
tesseract-ocr-eng \  
tesseract-ocr-nor && \  
pip install cython numpy && \  
pip install scipy && \  
pip install scikit-learn && \  
pip install paperwork && \  
mkdir -p /root/.local/share/ && \  
mkdir -p /root/.config && \  
ln -s /root/papers/.local /root/.local/share/paperwork && \  
ln -s /root/papers/.config/paperwork.conf /root/.config/paperwork.conf  
  
VOLUME ["/root/papers/"]  
ENTRYPOINT mkdir -p /root/papers/.local && mkdir -p /root/papers/.config &&
paperwork  

