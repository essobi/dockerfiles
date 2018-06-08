FROM wernight/phantomjs:latest  
LABEL maintainer "Fabrice Baumann"  
  
USER root  
WORKDIR /  
  
COPY report-mixed-content.js /opt/mixed-content-scanner/report-mixed-
content.js  
COPY scan /usr/local/bin/scan  
  
USER phantomjs  
CMD ["scan"]  

