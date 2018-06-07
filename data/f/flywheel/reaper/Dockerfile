FROM python:2.7-alpine as build  
  
RUN apk add --no-cache build-base  
  
ENV DCMTK_VERSION=3.6.2  
WORKDIR /src/dcmtk-$DCMTK_VERSION  
  
RUN wget -O -
http://dicom.offis.de/download/dcmtk/dcmtk${DCMTK_VERSION//./}/dcmtk-$DCMTK_VERSION.tar.gz
| tar xz -C /src  
  
COPY dcmtk.patch .  
RUN patch -p1 <dcmtk.patch  
  
RUN ./configure  
RUN make config-all ofstd-all oflog-all dcmdata-all dcmimgle-all dcmimage-all
dcmjpeg-all dcmjpls-all dcmtls-all dcmnet-all  
RUN make dcmdata-install dcmnet-install  
  
COPY . /src/reaper  
RUN python -m compileall /src/reaper/reaper && find /src/reaper/reaper -name
'*.py' -delete  
  
FROM python:2.7-alpine as dist  
  
RUN apk add --no-cache libstdc++ tzdata  
  
COPY \--from=build /usr/local/bin /usr/local/bin  
COPY \--from=build /usr/local/etc/dcmtk /usr/local/etc/dcmtk  
COPY \--from=build /usr/local/share/dcmtk /usr/local/share/dcmtk  
COPY \--from=build /usr/local/share/doc/dcmtk /usr/local/share/doc/dcmtk  
  
COPY requirements.txt /src/reaper/requirements.txt  
RUN pip install -r /src/reaper/requirements.txt  
  
COPY \--from=build /src/reaper /src/reaper  
RUN pip install -e /src/reaper  
  
CMD ["/bin/sh"]  
  
FROM dist as testing  
  
RUN pip install -r /src/reaper/tests/requirements.txt  

