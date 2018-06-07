FROM jodogne/orthanc-plugins:1.0.0  
RUN DEBIAN_FRONTEND=noninteractive apt-get update; apt-get -y install
libgdcm2-dev libjpeg-dev; rm -rf /var/lib/apt/lists/*  
  
ADD . /root/osimis-webviewer  
  
RUN bash /root/osimis-webviewer/scripts/dockerBuildWebViewer.sh "default"  
  
EXPOSE 4242  
EXPOSE 8042  
ENTRYPOINT [ "Orthanc" ]  
CMD [ "/etc/orthanc/orthanc.json" ]  

