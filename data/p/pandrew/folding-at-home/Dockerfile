FROM debian:jessie  
  
# If you set USERNAME to Anonymous, the folding@home client pauses for 5
minutes, but will then begin processing data.  
ENV USERNAME Anonymous  
ENV TEAM 0  
ENV POWER medium  
  
RUN apt-get update && apt-get -y install \  
curl \  
bzip2  
  
RUN curl -fL 'https://fah.stanford.edu/file-
releases/public/release/fahclient/debian-
testing-64bit/v7.4/fahclient_7.4.4_amd64.deb' > /fahclient.deb  
# Install Folding@home  
RUN dpkg -i /fahclient.deb  
ADD config.xml /etc/fahclient/  
RUN chown fahclient:root /etc/fahclient/config.xml  
RUN sed -i -e
"s/{{USERNAME}}/$USERNAME/;s/{{TEAM}}/$TEAM/;s/{{POWER}}/$POWER/"
/etc/fahclient/config.xml  
  
CMD FAHClient --config /etc/fahclient/config.xml  

