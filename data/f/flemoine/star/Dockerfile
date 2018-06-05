FROM ubuntu  
  
MAINTAINER Frederic Lemoine  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y wget  
  
RUN \  
wget -q https://github.com/alexdobin/STAR/archive/2.5.1b.tar.gz -O- \  
| tar xz -C /opt/ && \  
mkdir /opt/STAR && \  
cp /opt/STAR-2.5.1b/bin/Linux_x86_64_static/* /opt/STAR/ && \  
rm -rf /opt/STAR-2.5.1b/  
  
#  
# Finalize environment  
#  
RUN apt-get remove -q -y wget && apt-get autoremove -y  
ENV PATH
/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/opt/STAR/  

