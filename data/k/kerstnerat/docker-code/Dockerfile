FROM ubuntu:16.04  
# Environment variables  
ENV domain localhost  
ENV LC_CTYPE en_US.UTF-8  
# don't auto-generate default SSL cert as this causes problems on Debian 8 x64  
# ENV DONT_GEN_SSL_CERT true  
# Setup scripts for LibreOffice Online  
ADD /scripts/install-libreoffice.sh /  
ADD /scripts/start-libreoffice.sh /  
RUN bash install-libreoffice.sh  
  
# Entry point  
CMD bash start-libreoffice.sh  

