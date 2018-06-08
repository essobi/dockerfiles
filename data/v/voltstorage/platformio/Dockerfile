FROM python:2.7  
MAINTAINER David Bauske <david.bauske@voltstorage.com>  
  
WORKDIR /root  
  
RUN apt-get update  
  
RUN mkdir ~/.ssh  
RUN chmod 700 ~/.ssh  
  
RUN pip install platformio  
RUN pio platforms install espressif8266  
  
RUN git clone https://github.com/igrr/mkspiffs  
  
WORKDIR /root/mkspiffs  
RUN echo "cur: $(pwd)"  
RUN make dist  
RUN cp mkspiffs /bin/  
  
WORKDIR /root  
RUN rm -R mkspiffs

