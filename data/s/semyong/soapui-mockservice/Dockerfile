FROM openjdk:8  
RUN cd /opt && \  
wget -q
https://s3.amazonaws.com/downloads.eviware/soapuios/5.4.0/SoapUI-5.4.0-linux-
bin.tar.gz && \  
tar -zxf SoapUI-5.4.0-linux-bin.tar.gz  
ENV SOAPUI_HOME=/opt/SoapUI-5.4.0  
EXPOSE 80:8080  
ENTRYPOINT ["/opt/SoapUI-5.4.0/bin/mockservicerunner.sh"]  
CMD ["-p", "80", "/opt/SoapUI-5.4.0/HelloWS-soapui-project.xml"]  

