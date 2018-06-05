FROM alpine:3.2  
MAINTAINER Jérémy SEBAN <jeremy@seban.eu>  
  
# Installing software to compile  
RUN apk add --update gcc autoconf automake git g++ make python-dev openssl-dev
libffi-dev  
  
# Installing par2cmdline  
RUN git clone https://github.com/Parchive/par2cmdline /root/par2cmdline  
WORKDIR /root/par2cmdline  
RUN aclocal  
RUN automake --add-missing  
RUN autoconf  
RUN ./configure  
RUN make  
RUN make install  
  
# Installing other sabnzbd dependencies  
RUN apk add unrar unzip p7zip python openssl libffi  
  
# Installing python dependencies  
WORKDIR /root  
RUN curl https://bootstrap.pypa.io/get-pip.py > /root/pip.py  
RUN python /root/pip.py  
RUN pip install cheetah  
RUN pip install configobj  
RUN pip install feedparser  
RUN pip install pyOpenSSL  
# -- Installing python-yenc  
RUN curl http://www.golug.it/pub/yenc/yenc-0.3.tar.gz > /root/yenc-0.3.tar.gz  
RUN tar -xvzf yenc-0.3.tar.gz  
WORKDIR /root/yenc-0.3  
RUN python setup.py build  
RUN python setup.py install  
  
# Cloning sabnzbd  
WORKDIR /opt  
RUN git clone -b master https://github.com/sabnzbd/sabnzbd sabnzbd  
WORKDIR /opt/sabnzbd  
  
# Removing all software installed in order to compile par2  
RUN apk del gcc autoconf automake git g++ make python-dev openssl-dev libffi-
dev  
  
# Removing all download and package cache  
RUN rm -rf /var/cache/apk/*  
RUN rm -rf /root/par2cmdline  
RUN rm /root/pip.py  
RUN rm /root/yenc-0.3.tar.gz  
RUN rm -rf /root/yenc-0.3  
  
# Exposing sabnzbd web ui  
EXPOSE 8080  
# Define container volume  
VOLUME ["/config", "/downloads"]  
  
# Define environement variables, this is a hack since SABnzbd will store  
# its configuration in ~/.sabnzbd  
ENV HOME /config  
  
# Setting start CMD  
CMD ["/usr/bin/python", "/opt/sabnzbd/SABnzbd.py", "-f",
"/config/sabnzbd.ini", "-s", "0.0.0.0:8080"]  

