FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
## Picard  
RUN wget -O /tmp/picard-tools-1.139.zip
https://github.com/broadinstitute/picard/releases/download/1.139/picard-
tools-1.139.zip && \  
unzip /tmp/picard-tools-1.139.zip -d /usr/local/pipeline/ && \  
sed -i '$aCLASSPATH=.:$CLASSPATH:/usr/local/pipeline/picard-tools-1.139'
/home/snappy/.bashrc && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/picard-tools-1.139'
/home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/picard-tools-1.139 && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rvf /tmp/*  
  
CMD ["/bin/bash"]  

