FROM ubuntu:12.04.5  
MAINTAINER Albert Alvarez  
  
ENV LANG='es_ES.UTF-8' LANGUAGE='es_ES:es' LC_ALL='es_ES.UTF-8'  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install software-properties-common -y  
  
#RUN add-apt-repository -y ppa:libreoffice/ppa  
#RUN apt-get update  
RUN apt-get install -y libreoffice  
  
#RUN curl -fsSL
http://downloadarchive.documentfoundation.org/libreoffice/old/3.6.4.3/deb/x86_64/*
-o /libre/  
#RUN curl -fsSL
http://downloadarchive.documentfoundation.org/libreoffice/old/3.6.4.3/deb/x86_64/LibO-
SDK_3.6.4.3_Linux_x86-64_install-deb_en-US.tar.gz -o /tmp/libre.tar.gz  
#RUN curl -fsSL https://libreoffice.en.uptodown.com/ubuntu/download/40076 -o
/tmp/libre.gz  
#RUN chmod +x /tmp/libre.gz  
#RUN tar -zxvf /tmp/libre.gz  
#  
#RUN cd /Lib*/DEBS  
#RUN dpkg -i /Lib*/DEBS/*.deb  
#RUN dpkg -i /Lib*/DEBS/desktop-integration/*.deb  
#RUN rm /tmp/libre.tar.gz  
#RUN chmod +x $(ls | grep Lib)/DEBS/$(ls $(ls | grep Lib)/DEBS)  
#RUN chmod +x $(ls | grep Lib)/DEBS/*.gz  
#RUN dpkg --force-depends -i $(ls | grep Lib)/DEBS/*.gz  
#  
#RUN apt-get update  
#RUN apt-get -y install -f --no-install-recommends  
#  
#RUN rm -fR /tmp/*  
RUN apt-get install libreoffice-sdbc-postgresql -y  
RUN apt-get install -y unixodbc-dev libmyodbc  
  
CMD libreoffice  

