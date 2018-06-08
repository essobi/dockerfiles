FROM python:2-alpine3.7 as build  
  
RUN apk add --no-cache build-base  
  
ENV DCMTK_VERSION=3.6.2  
WORKDIR /src/dcmtk-$DCMTK_VERSION  
  
RUN wget -O -
http://dicom.offis.de/download/dcmtk/dcmtk${DCMTK_VERSION//./}/dcmtk-$DCMTK_VERSION.tar.gz
| tar xz -C /src  
  
RUN ./configure  
RUN make all && make install  
  
RUN pip install ipython  
RUN pip install "pydicom==0.9.9"  
  
FROM python:2-alpine3.7  
RUN apk add --no-cache libstdc++  
  
COPY \--from=build /usr/local/bin /usr/local/bin  
COPY \--from=build /usr/local/etc/dcmtk /usr/local/etc/dcmtk  
COPY \--from=build /usr/local/share/dcmtk /usr/local/share/dcmtk  
COPY \--from=build /usr/local/share/doc/dcmtk /usr/local/share/doc/dcmtk  
  
COPY \--from=build /usr/local/lib/python2.7/site-packages
/usr/local/lib/python2.7/site-packages  
  
WORKDIR /data  
  
CMD ["/bin/sh"]  

