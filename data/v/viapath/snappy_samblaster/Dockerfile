FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# samblaster (duplicate marking and split/discordant extraction)  
RUN cd /tmp && \  
git clone git://github.com/GregoryFaust/samblaster.git && \  
cd samblaster && git checkout v.0.1.22 && \  
make && \  
mkdir -p /usr/local/pipeline/samblaster && \  
cp samblaster /usr/local/pipeline/samblaster/ && \  
chmod -R 755 /usr/local/pipeline/samblaster && \  
ln -s /usr/local/pipeline/samblaster/samblaster /usr/local/bin/ && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/samblaster' /home/snappy/.bashrc && \  
chmod -R 755 /usr/local/pipeline/samblaster && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rf /tmp/*  
  
CMD ["/bin/bash"]  

