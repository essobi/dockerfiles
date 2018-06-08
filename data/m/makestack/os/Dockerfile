# docker build -t makestack/os .  
# docker run -v $PWD/examples/led-blink:/app -t makestack/os  
FROM ubuntu:16.04  
MAINTAINER Seiya Nuta <nuta@seiya.me>  
  
WORKDIR /tmp  
  
RUN sed -i -e
's#http://archive.ubuntu.com/ubuntu/#mirror://mirrors.ubuntu.com/mirrors.txt#'
/etc/apt/sources.list  
RUN apt-get update && apt-get install -qy build-essential zsh git python3-pip
ruby git wget  
  
# xtensa toolchain  
RUN wget -O - -q http://arduino.esp8266.com/linux64-xtensa-lx106-elf-
gb404fb9.tar.gz | tar zxf - -C /usr/local  
ENV PATH=/usr/local/xtensa-lx106-elf/bin:$PATH  
  
# MakeStack CLI  
RUN git clone https://github.com/makestack/cli && \  
cd cli && \  
python3 setup.py install  
  
RUN useradd makestack  
  
ADD . /os  
WORKDIR /os  
RUN chown -R makestack /os  
RUN pip3 install -r requirements.txt  
RUN pip3 install -r resea/requirements.txt  
  
USER makestack  
RUN git submodule update --init  
RUN make prebuild ARCH=esp8266  
CMD unzip -n /app/app.zip -d /app && make build APP_DIR=/app  

