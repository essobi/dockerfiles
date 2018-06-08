FROM golang:1.5  
MAINTAINER Etienne Trimaille <etienne@kartoza.com>  
  
RUN apt-get update && apt-get install -y python-pip \  
libprotobuf-dev libleveldb-dev libgeos-dev \  
libpq-dev python-dev \  
libyaml-dev\  
\--no-install-recommends  
  
ENV TIME 120  
ENV USER docker  
ENV PASSWORD docker  
ENV DATABASE gis  
ENV HOST db  
ENV PORT 5432  
ENV SETTINGS /PBF  
ENV CACHE cache  
ENV IMPORT_DONE import_done  
ENV IMPORT_QUEUE import_queue  
ENV SRID 4326  
ENV OPTIMIZE false  
ENV DBSCHEMA_PRODUCTION public  
ENV DBSCHEMA_IMPORT import  
ENV DBSCHEMA_BACKUP backup  
  
RUN ln -s /usr/lib/libgeos_c.so /usr/lib/libgeos.so  
  
WORKDIR $GOPATH  
RUN go get github.com/tools/godep  
RUN git clone https://github.com/omniscale/imposm3
src/github.com/omniscale/imposm3  
RUN cd src/github.com/omniscale/imposm3 && godep go install ./...  
  
ADD requirements.txt /home/requirements.txt  
RUN pip install -r /home/requirements.txt  
  
ADD importer.py /home/  
  
RUN mkdir /home/cache  
  
VOLUME ["/PBF"]  
WORKDIR /home  
CMD ["python", "-u", "/home/importer.py"]  

