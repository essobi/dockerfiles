FROM deeplearninc/spark  
  
LABEL vendor="DeepLearn Inc"  
  
COPY requirements.txt .  
COPY requirements.test.txt .  
COPY requirements.worker.txt .  
  
RUN apt-get -qq update \  
&& apt-get -qq --no-install-recommends install build-essential cmake python-
setuptools python-pip python-dev  
  
RUN git clone --recursive https://github.com/dmlc/xgboost.git \  
&& cd xgboost \  
&& make -j 4 \  
&& mkdir /usr/xgboost \  
&& cp lib/libxgboost.so /usr/xgboost/libxgboost.so  
  
RUN pip download --dest=/root/pip_packages \  
wheel \  
-r requirements.txt \  
-r requirements.test.txt \  
-r requirements.worker.txt \  
xgboost/python-package \  
&& pip install --no-index --find-links=/root/pip_packages wheel \  
&& pip install --no-index --find-links=/root/pip_packages \  
-r requirements.txt \  
-r requirements.test.txt \  
-r requirements.worker.txt \  
xgboost/python-package  

