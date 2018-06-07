FROM base/archlinux  
MAINTAINER sventopia <sventopia@me.com>  
RUN pacman -Sy  
RUN pacman -S --noconfirm net-tools python python-pip git  
RUN pip install requests IPy  
RUN cd opt; git clone https://github.com/sventopia/hello_heidi.git  
RUN chmod +x /opt/hello_heidi/helloHeidi.py  

