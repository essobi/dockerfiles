FROM viapath/snappy_base:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# trimmomatic  
RUN wget --no-verbose -O /tmp/Trimmomatic-0.32.zip
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.32.zip
&& \  
unzip /tmp/Trimmomatic-0.32.zip -d /usr/local/pipeline/ && \  
sed -i
'$aCLASSPATH=.:$CLASSPATH:/usr/local/pipeline/Trimmomatic-0.32/trimmomatic-0.32.jar'
/home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/Trimmomatic-0.32 && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rvf /tmp/*  
  
CMD ["/bin/bash"]  

