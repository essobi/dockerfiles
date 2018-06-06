FROM ubuntu:16.04  
  
#ENV http_proxy "http://proxy.materna.de:8080"  
#ENV https_proxy "http://proxy.materna.de:8080"  
RUN apt-get update && apt-get install --yes \  
apt-utils \  
sudo \  
make \  
gcc-avr \  
binutils \  
avr-libc \  
avrdude \  
arduino-mk \  
python-pip \  
python3-dev \  
nano  
RUN pip install --upgrade pip  
RUN pip install pyserial  
  
USER root  
  
RUN useradd -ms /bin/bash dragana  
RUN adduser dragana dialout  
RUN adduser dragana uucp  
RUN adduser dragana sudo  
RUN adduser dragana root  
  
RUN sudo \--user=dragana mkdir -p
/home/dragana/Dokumente/repos_git/modules/config/configurationsystem/Arduino_Docker_Temp  
  
COPY .
/home/dragana/Dokumente/repos_git/modules/config/configurationsystem/Arduino_Docker_Temp  
RUN chown root:root /etc/sudoers && chmod 440 /etc/sudoers  
COPY . /usr/  
  
#COPY . /etc/sudoers  
#RUN chown root:root /etc/sudoers && chmod 440 /etc/sudoers  
RUN chmod +x
/home/dragana/Dokumente/repos_git/modules/config/configurationsystem/Arduino_Docker_Temp/run.sh  
  
USER dragana  
CMD
/home/dragana/Dokumente/repos_git/modules/config/configurationsystem/Arduino_Docker_Temp/run.sh  

