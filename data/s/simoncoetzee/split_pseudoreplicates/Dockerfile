FROM ubuntu:14.04  
  
MAINTAINER Simon Coetzee "simon.coetzee@cshs.org"  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y upgrade \  
&& apt-get install -y wget bedtools samtools \  
&& apt-get clean  
  
COPY run.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/run.sh  
VOLUME /data  
CMD ["run.sh"]  

