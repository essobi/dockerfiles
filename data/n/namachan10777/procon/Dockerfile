# set the base image  
FROM ubuntu  
  
# author  
MAINTAINER Nakano Masaki  
  
# basic  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get install -qy apt-utils  
RUN apt-get install -qy git  
RUN apt-get install -qy curl  
RUN apt-get install -qy xz-utils  
RUN apt-get install -qy tar  
RUN apt-get install -qy wget  
  
# g++ 7.x ppa repository  
RUN apt-get install -qy software-properties-common  
RUN add-apt-repository ppa:jonathonf/gcc-7.1  
RUN apt-get update  
  
# C++ setting  
RUN apt-get install -qy m4  
RUN apt-get install -qy g++-7  
RUN apt-get install -qy make  
RUN apt-get install -qy cmake  
  
# dlang setting  
RUN curl -fsS https://dlang.org/install.sh | bash -s dmd  
RUN sh ~/dlang/dmd-2.076.0/activate  
RUN apt-get install -qy dub  
RUN echo 'source ~/dlang/dmd-2.076.0/activate' >> ~/.bashrc  
  
# solver namachan dependencies  
RUN apt-get install -qy libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev
libsdl2-net-dev libsdl2-ttf-dev  
RUN apt-get install -qy libcurl4-gnutls-dev  
  
RUN dub fetch derelict-sdl2 --version=2.0.2  
  
# python setting  
RUN apt-get install -qy python3  
RUN apt-get install -qy python3-pip  
RUN pip3 install --upgrade pip  
# python packages  
RUN pip3 install PyYAML  
RUN pip3 install jsonschema  
RUN pip3 install pyqt5  
  
RUN mkdir ci  
  
WORKDIR ci  
  
ENTRYPOINT ["/bin/bash"]  

