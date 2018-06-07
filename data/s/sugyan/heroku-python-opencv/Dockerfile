# Inherit from Heroku's python stack  
FROM heroku/python  
  
# Install OpenCV  
RUN mkdir -p /app/.heroku/opencv /tmp/opencv  
ADD Install-OpenCV /tmp/opencv  
WORKDIR /tmp/opencv/Ubuntu  
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty multiverse' >>
/etc/apt/sources.list && apt-get update  
RUN ./opencv_latest.sh  
  
# Python environment  
RUN echo 'export
PYTHONPATH=${PYTHONPATH:-/app/.heroku/opencv/lib/python2.7/site-packages}' >
/app/.profile.d/opencv.sh  
  
ONBUILD WORKDIR /app/user  
ONBUILD ADD requirements.txt /app/user/  
ONBUILD RUN /app/.heroku/python/bin/pip install -r requirements.txt  
ONBUILD ADD . /app/user/  

