ARG version=xenial  
  
FROM ubuntu:${version}  
  
LABEL maintainer="frank.foerster@ime.fraunhofer.de"  
LABEL description="Dockerfile providing the HISAT2 mapping software"  
  
RUN apt-get update && apt-get -y install \  
wget \  
python \  
gzip \  
tar  
  
WORKDIR /opt  
  
RUN wget \  
-O /tmp/cufflinks.tar.gz \  
'http://cole-trapnell-
lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz'
&& \  
tar xzf /tmp/cufflinks.tar.gz && \  
rm /tmp/cufflinks.tar.gz  
  
ENV PATH "$PATH:/opt/cufflinks-2.2.1.Linux_x86_64/"  
VOLUME /data  
  
WORKDIR /data  
  
CMD cufflinks --help  

