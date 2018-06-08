FROM buildpack-deps:jessie-scm  
  
RUN apt-get update && \  
apt-get install -q -y python build-essential && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone \--depth 1 --recursive -b master
https://github.com/meteor/meteor.git /opt/meteor && \  
ln -s /opt/meteor/meteor /usr/local/bin/meteor && \  
meteor help \--unsafe-perm && \  
meteor npm cache clear && \  
rm -rf /tmp/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

