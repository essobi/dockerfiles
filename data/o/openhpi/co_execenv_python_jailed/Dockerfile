FROM ubuntu:14.04  
MAINTAINER "Martin v. Löwis, Thomas Staubitz, Andrey Sapegin"  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ADD assess.py /usr/lib/python3.4/assess.py  
ADD webpython.py /usr/lib/python3.4/webpython.py  
RUN rm /usr/lib/python3.4/turtle.py  
ADD turtle.py /usr/lib/python3.4/turtle.py  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y wget make python2.7 gcc  
RUN wget http://olivier.sessink.nl/jailkit/jailkit-2.19.tar.gz  
RUN tar -xzvf jailkit-2.19.tar.gz  
  
ENV PYTHONINTERPRETER /usr/bin/python2.7  
  
RUN cd jailkit-2.19; ./configure; make; make install  
RUN echo "" >> /etc/jailkit/jk_init.ini  
RUN echo "[python3.4_jk]" >> /etc/jailkit/jk_init.ini  
RUN echo "paths = python3.4, /usr/local/lib/python3.4, /usr/lib/python3.4,
/etc/ld.so.conf, /workspace" >> /etc/jailkit/jk_init.ini  
RUN echo "devices = /dev/null, /dev/zero, /dev/random, /dev/urandom " >>
/etc/jailkit/jk_init.ini  
  
RUN adduser --disabled-password --no-create-home --gecos Python python  
  
RUN sed -i "1s/.*/\\#\\!\/usr\/bin\/python2.7/" /usr/sbin/jk_init  
  
RUN jk_init -v -j /home/jail_py python3.4_jk  
  
ENV PYTHONPATH /usr/lib/python3.4:/workspace  
ENV PATH $PATH:/usr/lib/python3.4  

