FROM zoobab/ubuntu-oneiric-11.10-x86_64  
  
RUN sed -i -re 's/([a-z]{2}\\.)?archive.ubuntu.com|security.ubuntu.com/old-
releases.ubuntu.com/g' /etc/apt/sources.list  
RUN apt-get -fq update  
  
ADD MxEasy_1.4.1-ubuntu-11.10_amd64.deb .  
ADD run.sh /root  
RUN chmod +x /root/run.sh  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -s /bin/true /sbin/initctl  
RUN apt-get install -y libglu1-mesa libxrender1 libsm6 libjack0 libmxml1  
RUN dpkg -i MxEasy_1.4.1-ubuntu-11.10_amd64.deb; apt-get -f -y install  
RUN ldconfig  
  
CMD /root/run.sh  

