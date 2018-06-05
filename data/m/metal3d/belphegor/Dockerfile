FROM fedora:22  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
ENV NUMWORKER 4  
EXPOSE 8000  
RUN dnf install -y python-pip python-qt4 Xvfb which \  
xorg-x11-fonts-100dpi \  
xorg-x11-fonts-ISO8859-1-100dpi \  
xorg-x11-fonts-Type1 \  
xorg-x11-fonts-misc \  
&& dnf clean all  
  
RUN pip install Ghost.py gunicorn  
  
RUN mkdir -p /root/rpmbuild/specs  
ADD msttcorefonts-2.5-1.spec /root/rpmbuild/spec/msttcorefonts-2.5-1.spec  
ADD msfont.sh /opt/msfont.sh  
ADD entrypoint.sh /usr/local/bin/entrypoint  
  
COPY belphegor/main.py /opt/main.py  
WORKDIR /opt  
ENTRYPOINT ["/bin/bash", "/usr/local/bin/entrypoint"]  
CMD xvfb-run -s "-screen 0 1024x768x24" gunicorn -b 0.0.0.0:8000 -w $NUMWORKER
main:app  
  

