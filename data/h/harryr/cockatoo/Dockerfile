FROM harryr/cockatoo:virtualbox5  
MAINTAINER Harry Roberts <harry.roberts@xiphosresearch.co.uk>  
  
RUN apt-get -y install mkisofs genisoimage python2.7 python-pip dmidecode lshw
sudo gcc-mingw-w64-i686 libffi-dev  
  
RUN apt-get -y install libssl-dev  
  
RUN mkdir -p /mnt/isos/ /.vmcloak/  
COPY makevm.sh /makevm.sh  
  
VOLUME /.vmcloak/  
VOLUME /mnt/isos  
  
COPY vmcloak/requirements.txt /root/vmcloak-requirements.txt  
RUN pip install -r /root/vmcloak-requirements.txt  
  
COPY vmcloak /root/src  
RUN cd /root/src && make -C utils && python setup.py install  
  
CMD ["/root/makevm.sh"]  

