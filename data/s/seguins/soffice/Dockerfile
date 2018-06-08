FROM java:jre  
  
RUN apt-get update  
RUN apt-get install -y libxt6 libxrender1  
RUN apt-get clean  
  
WORKDIR /tmp  
  
RUN wget
http://netcologne.dl.sourceforge.net/project/openofficeorg.mirror/4.1.1/binaries/en-
US/Apache_OpenOffice_4.1.1_Linux_x86-64_install-deb_en-US.tar.gz  
RUN tar xf Apache_OpenOffice_4.1.1_Linux_x86-64_install-deb_en-US.tar.gz  
  
WORKDIR /tmp/en-US/DEBS  
  
RUN dpkg -i *.deb  
  
WORKDIR /opt/openoffice4/program  
  
RUN rm -rf /tmp/en-US /tmp/Apache_OpenOffice_4.1.1_Linux_x86-64_install-
deb_en-US.tar.gz  
  
RUN useradd -ms /bin/bash soffice  
USER soffice  
  
EXPOSE 8100  
CMD ./soffice -headless -accept="socket,host=0.0.0.0,port=8100;urp;"
-nofirststartwizard  

