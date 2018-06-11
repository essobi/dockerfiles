FROM ubuntu:14.04.2  
MAINTAINER Doro Wu <fcwu.tw@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN apt-get update \  
&& apt-get install -y --force-yes --no-install-recommends supervisor \  
openssh-server pwgen sudo vim-tiny \  
net-tools \  
xfce4 x11vnc xvfb default-jre \  
gtk2-engines-murrine ttf-ubuntu-font-family \  
nginx python-pip python-dev build-essential \  
unzip software-properties-common \  
python-software-properties  
RUN apt-add-repository ppa:alessandro-strada/ppa  
RUN apt-get update  
RUN apt-get install -y fuse  
RUN apt-get install -y google-drive-ocamlfuse  
  
ADD
https://dl.dropboxusercontent.com/u/23905041/x11vnc_0.9.14-1.1ubuntu1_amd64.deb
/tmp/  
ADD https://dl.dropboxusercontent.com/u/23905041/x11vnc-
data_0.9.14-1.1ubuntu1_all.deb /tmp/  
RUN dpkg -i /tmp/x11vnc*.deb  
  
# Pulls nand2tetris.zip from site, unzips and configures software tools  
ADD http://nand2tetris.org/software/nand2tetris.zip /nand2tetris/  
RUN unzip /nand2tetris/nand2tetris.zip && rm -fr /nand2tetris/nand2tetris.zip  
RUN ln -s /nand2tetris/tools/HardwareSimulator.sh /bin/HardwareSimulator  
RUN ln -s /nand2tetris/tools/CPUEmulator.sh /bin/CPUEmulator  
RUN chmod +x /bin/HardwareSimulator && chmod +x /bin/CPUEmulator  
  
ADD web /web/  
RUN pip install -r /web/requirements.txt  
  
ADD noVNC /noVNC/  
ADD nginx.conf /etc/nginx/sites-enabled/default  
ADD startup.sh /  
ADD supervisord.conf /etc/supervisor/conf.d/  
  
RUN adduser ubuntu  
RUN chpasswd ubuntu:ubuntu  
RUN adduser ubuntu sudo  
RUN adduser ubuntu fuse  
  
RUN chgrp fuse /dev/fuse  
RUN chmod g+rw /dev/fuse  
  
ADD mount-script.py /home/ubuntu/  
  
RUN apt-get install -y xterm firefox  
  
VOLUME /c/Users/docker/:/home/ubuntu/storage  
  
EXPOSE 6080  
WORKDIR /root  
ENTRYPOINT ["/startup.sh"]  

