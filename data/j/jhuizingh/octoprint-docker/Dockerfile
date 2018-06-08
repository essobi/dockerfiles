FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-pip \  
python-dev \  
git \  
build-essential \  
libav-tools \  
avrdude \  
curl  
  
RUN apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /cura-engine  
RUN apt-get update && apt-get -y install gcc-4.7 g++-4.7 wget  
RUN git clone -b legacy https://github.com/Ultimaker/CuraEngine.git  
WORKDIR /cura-engine/CuraEngine  
RUN wget http://bit.ly/curaengine_makefile_patch -O CuraEngine.patch  
RUN patch < CuraEngine.patch && git diff  
RUN make CXX=g++-4.7  
  
WORKDIR /octoprint  
RUN git clone https://github.com/foosel/OctoPrint.git /octoprint  
RUN pip install --upgrade pip  
RUN pip install setuptools  
RUN pip install -r requirements.txt  
RUN python setup.py install  
  
VOLUME /data  
VOLUME /usr/lib/python2.7/dist-packages  
WORKDIR /data  
EXPOSE 5000  
CMD ["octoprint", "--iknowwhatimdoing", "--basedir" ,"/data"]  

