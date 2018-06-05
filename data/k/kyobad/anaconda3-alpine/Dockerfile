FROM frolvlad/alpine-glibc:latest  
  
MAINTAINER K.Kato  
  
ENV PATH=/opt/conda/bin:$PATH \  
ANACONDA=Anaconda3-4.2.0-Linux-x86_64.sh  
  
RUN apk add --no-cache --virtual=build-deps --update-cache \  
wget bash \  
&& wget -q --no-check-certificate https://repo.continuum.io/archive/$ANACONDA
\  
&& /bin/bash $ANACONDA -b -p /opt/conda \  
&& rm -rf /root/.continuum /opt/conda/pkgs/* \  
&& rm $ANACONDA \  
&& apk del build-deps \  
&& mkdir /root/notebook  
  
WORKDIR /root/notebook/  
  
CMD ["/bin/sh", "-c", "jupyter notebook --no-browser --port=8888
--ip=0.0.0.0"]  
  

