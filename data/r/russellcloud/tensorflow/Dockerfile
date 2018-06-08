FROM russellcloud/opencv:latest-py2  
MAINTAINER RussellCloud Team "support@russellcloud.cn"  
ARG KERAS_VERSION=1.2.2  
RUN pip install --upgrade tensorflow==1.0.0  
  
RUN pip --no-cache-dir install
git+git://github.com/fchollet/keras.git@${KERAS_VERSION}

