FROM brimstone/ubuntu:14.04  
RUN package duplicity python-swiftclient  
  
ADD https://raw.githubusercontent.com/alkivi-sas/duplicity-
hubic/github/hubicbackend.py /usr/lib/python2.7/dist-
packages/duplicity/backends/hubicbackend.py  
  
ADD https://raw.githubusercontent.com/puzzle1536/hubic-wrapper-to-
swift/master/hubic.py /usr/local/bin/hubic  
  
RUN chmod 755 /usr/local/bin/hubic  
  
ENTRYPOINT ["/usr/bin/duplicity"]  

