FROM gliderlabs/alpine:3.2  
RUN apk --update add curl py-pip  
  
RUN curl -O https://webops-assets.getpebble.com/tools/DenyHosts-2.6.tar.gz &&
\  
tar xzvf DenyHosts-2.6.tar.gz && \  
cd DenyHosts-2.6 && \  
python setup.py install  
  
COPY denyhosts.cfg /usr/share/denyhosts/denyhosts.cfg  
  
CMD python /DenyHosts-2.6/daemon-control-dist start

