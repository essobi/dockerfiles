FROM maven:3.5.0-jdk-9  
ENV GAUGE_VERSION=0.8.3  
#RUN echo "export GAUGE_ROOT=/usr/local/" >> ~/.profile  
RUN rm -f /root/.profile  
ADD .profile /root/  
ENV GAUGE_ROOT=/usr/local/  
RUN wget
https://github.com/getgauge/gauge/releases/download/v${GAUGE_VERSION}/gauge-${GAUGE_VERSION}-linux.x86_64.zip
-P /tmp  
RUN unzip /tmp/gauge-${GAUGE_VERSION}-linux.x86_64.zip -d /tmp/gauge  
RUN cd /tmp/gauge && ./install.sh  
RUN gauge --install java && gauge --install html-report && gauge --install
xml-report  
CMD [ "gauge", "-v" ]  
  

