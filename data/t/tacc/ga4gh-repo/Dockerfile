  
FROM afirth/ga4gh-server:latest  
MAINTAINER Matthew Vaughn <vaughn@tacc.utexas.edu>  
  
ENV UID 1002  
ENV GID 1002  
ENV UNAME repo_admin  
  
RUN apt-get -y update && \  
apt-get -y install libncurses-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /home/$UNAME && \  
groupadd -r $UNAME -g $GID && \  
useradd -u $UID -r -g $UNAME -d /home/$UNAME -s /sbin/nologin -c "GA4GH repo
admin" $UNAME && \  
chown -R $UNAME:$UNAME /home/$UNAME  
  
RUN cd /tmp && \  
wget
https://github.com/samtools/htslib/releases/download/1.2.1/htslib-1.2.1.tar.bz2
&& \  
tar xf htslib-1.2.1.tar.bz2 && \  
cd htslib-1.2.1 && \  
make && make install && \  
cd ../ && rm -rf htslib-1.2.1*  
  
RUN cd /tmp && \  
wget
https://github.com/samtools/samtools/releases/download/1.2/samtools-1.2.tar.bz2
&& \  
tar xf samtools-1.2.tar.bz2 && \  
cd samtools-1.2 && \  
make && make install && \  
cd ../ && rm -rf samtools-1.2*  
  
RUN cd /tmp && \  
wget
https://github.com/samtools/bcftools/releases/download/1.2/bcftools-1.2.tar.bz2
&& \  
tar xf bcftools-1.2.tar.bz2 && \  
cd bcftools-1.2 && \  
make && make install && \  
cd ../ && rm -rf bcftools-1.2*  
  
USER $UNAME  
WORKDIR /home/$UNAME  
  
ENTRYPOINT /bin/bash  
  

