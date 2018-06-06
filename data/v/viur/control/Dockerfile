FROM viur/viur-env  
MAINTAINER http://www.viur.is  
WORKDIR /src  
ADD . .  
  
CMD ["/usr/bin/vc_start"]  
  
RUN git clone \--recursive https://bitbucket.org/viur/control.git
/src/viur_control && \  
cd /src/viur_control && \  
python setup.py install && \  
cp /src/scripts/vc_start.sh /usr/bin/vc_start && \  
chmod +x /usr/bin/vc_start  
  
VOLUME ["/Projects"]  
  
EXPOSE 5000 8000 8080  

