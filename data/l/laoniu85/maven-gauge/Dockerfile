FROM maven:3.3.9-jdk-8  
RUN echo "export GAUGE_ROOT=/usr/local/" >> ~/.profile && \  
export GAUGE_ROOT=/usr/local/ && cd /tmp && \  
wget
https://github.com/getgauge/gauge/releases/download/v0.6.2/gauge-0.6.2-linux.x86_64.zip
&& \  
unzip gauge-0.6.2-linux.x86_64.zip -d gauge && \  
cd /tmp/gauge && ./install.sh && \  
gauge \--install java && gauge \--install html-report && gauge \--install xml-
report  
  
  

