FROM phusion/baseimage  
  
MAINTAINER Nay San <nay.san@anu.edu.au>  
  
RUN apt-get update  
  
RUN apt-get install -y \  
git \  
python3-pip \  
libfftw3-dev \  
ffmpeg \  
libavcodec-dev  
  
WORKDIR /usr/bin  
  
RUN ln -s pip3 pip \  
&& ln -s python3 python  
  
RUN pip install --upgrade pip \  
&& pip install numpy \  
&& pip install pyfftw  
  
WORKDIR /  
  
RUN git clone https://fauxneticien@gitlab.com/fauxneticien/av_align.py.git
/tmp/av_align \  
&& mv /tmp/av_align/av_align.py /av_align.py  

