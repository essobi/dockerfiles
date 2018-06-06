FROM grzanka/ubuntu_vnc_ssh  
MAINTAINER Leszek Grzanka <grzanka@agh.edu.pl>  
  
# Install libraries  
RUN echo "test\n" | /usr/bin/sudo -S bash -c "apt-get update && apt-get
install -y \  
python3-pip \  
python3-numpy python3-scipy python3-matplotlib \  
python3-pyqt5 \  
&& rm -rf /var/lib/apt/lists/*"  
  
# Install python packages  
RUN echo "test\n" | /usr/bin/sudo -S pip3 install pydicom  
  
# Make directory to host tests  
RUN mkdir -p ~/git  
  
# clone some example repository  
RUN cd ~/git && git clone https://github.com/Programmica/pyqt5-tutorial.git  
  
CMD echo "test\n" | /usr/bin/sudo -S /usr/bin/supervisord -c
/etc/supervisor/supervisord.conf && bash  

