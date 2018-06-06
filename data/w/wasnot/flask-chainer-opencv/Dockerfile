FROM tiangolo/uwsgi-nginx-flask:flask  
  
RUN \  
pip install -U setuptools pip && \  
pip install chainer==1.6.2.1 && \  
pip install numpy==1.11.1 && \  
pip install scipy==0.15.1 && \  
pip install scikit-learn==0.17.1 && \  
pip install pandas==0.18.1  
  
RUN \  
apt-get update && apt-get upgrade -y && \  
apt-get install libopencv-dev python-opencv -y  
  
RUN ln -s /usr/lib/python2.7/dist-packages/cv2.x86_64-linux-gnu.so
/usr/local/lib/python2.7/site-packages/cv2.so  
  

