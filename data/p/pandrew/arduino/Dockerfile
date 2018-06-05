FROM java  
  
RUN apt-get update && apt-get -y install \  
\--no-install-recommends \  
xz-utils \  
execstack  
  
RUN cd /lib/x86_64-linux-gnu \  
&& ln -s libc.so.6 libc.so  
  
ENV ARDUINO_VERSION 1.6.4  
RUN curl -fL
http://downloads.arduino.cc/arduino-${ARDUINO_VERSION}-linux64.tar.xz -o
/arduino.tar.xz \  
&& tar xvf /arduino.tar.xz \  
&& mv /arduino-${ARDUINO_VERSION} /arduino  
  
WORKDIR /arduino  
ENTRYPOINT ["./arduino"]  

