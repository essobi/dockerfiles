FROM ubuntu:14.04  
ADD https://apt.mopidy.com/mopidy.gpg /mopidy.gpg  
ADD https://apt.mopidy.com/mopidy.list /etc/apt/sources.list.d/mopidy.list  
  
RUN cat /mopidy.gpg | sudo apt-key add -  
  
RUN apt-get update && apt-get install -y portaudio19-dev \  
python-pyaudio \  
python-pip \  
python-dev \  
libffi-dev \  
libspotify-dev \  
libasound2-dev \  
libevent-dev  
  
RUN mkdir /fm  
  
ADD . /fm  
  
WORKDIR /fm  
  
RUN python setup.py install  
  
CMD fm-player  

