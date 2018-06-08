FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# bamUtil (including libStatGen)  
RUN cd /tmp && \  
git clone https://github.com/statgen/libStatGen.git && \  
cd libStatGen && \  
git checkout v1.0.13 && \  
make all && \  
make install && \  
cd /tmp && \  
git clone https://github.com/statgen/bamUtil.git && \  
cd bamUtil && \  
git checkout v1.0.13 && \  
make install INSTALLDIR=/usr/local/pipeline/bamUtil_1.0.12 && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/bamUtil_1.0.12' /home/snappy/.bashrc
&& \  
ln -s /usr/local/pipeline/bamUtil_1.0.12/bam /usr/bin/local && \  
chmod -R 755 /usr/local/pipeline && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rvf /tmp/*  
  
CMD ["/bin/bash"]  

