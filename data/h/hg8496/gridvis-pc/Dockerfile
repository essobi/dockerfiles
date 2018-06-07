FROM ubuntu  
  
ENV VERSION 7.1.10  
RUN apt-get update \  
&& apt-get install -y xrdp xvfb wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN wget -q -O GridVis.sh
http://gridvis.janitza.de/download/$VERSION/GridVis-$VERSION-64bit.sh \  
&& sh GridVis.sh -q \  
&& rm GridVis.sh \  
&& ln -s /opt/GridVisData/license2-pc.lic /usr/local/GridVis/license2.lic  
  
RUN adduser --disabled-password --gecos "" gridvis  
RUN adduser gridvis sudo  
RUN adduser gridvis users  
RUN echo "gridvis:gridvispwd" | chpasswd  
  
ADD xrdp.ini /etc/xrdp/  
ADD start.sh /  
COPY xsession /home/gridvis/.xsession  
  
CMD /start.sh  
  
# for RDP  
EXPOSE 3389  
VOLUME ["/opt/GridVisProjects"]  

