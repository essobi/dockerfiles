FROM java:8  
LABEL maintainer="tw@touk.pl"  
  
# copied from lanrat/xpra-html5  
RUN apt-get update && \  
apt-get install -y apt-utils wget && \  
wget -O - http://winswitch.org/gpg.asc | apt-key add - && \  
echo "deb http://winswitch.org/ jessie main" >
/etc/apt/sources.list.d/xpra.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y xpra xvfb xterm && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget -O -
http://cdn01.downloads.smartbear.com/soapui/5.3.0/SoapUI-5.3.0-linux-
bin.tar.gz | tar -zx -C /opt/  
  
RUN adduser --disabled-password --gecos "SoapUI" \--uid 1000 soapui && chown
1000.1000 -R /home/soapui  
USER soapui  
WORKDIR /home/soapui  
VOLUME /home/soapui  
  
EXPOSE 10001  
ENV DISPLAY=:100  
CMD xpra start --bind-tcp=0.0.0.0:10001 --html=on --start-
child=/opt/SoapUI-5.3.0/bin/soapui.sh --exit-with-children --daemon=no
--xvfb="/usr/bin/Xvfb +extension Composite -screen 0 1920x1080x24+32 -nolisten
tcp -noreset" \--pulseaudio=no --notifications=no --bell=no  

