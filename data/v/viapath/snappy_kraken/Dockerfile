FROM viapath/snappy_base:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# kraken  
RUN cd /tmp && \  
git clone \--recursive https://github.com/DerrickWood/kraken.git && \  
cd /tmp/kraken && git checkout adfaa267ebdc9f16946fa4a19ddb1bb6e7cb5a97 && \  
sh install_kraken.sh /usr/local/pipeline/kraken && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/kraken' /home/snappy/.bashrc && \  
ln -s /usr/local/pipeline/kraken/kraken /usr/local/bin/ && \  
ln -s /usr/local/pipeline/kraken/kraken-build /usr/local/bin/ && \  
ln -s /usr/local/pipeline/kraken/kraken-filter /usr/local/bin/ && \  
ln -s /usr/local/pipeline/kraken/kraken-mpa-report /usr/local/bin/ && \  
ln -s /usr/local/pipeline/kraken/kraken-report /usr/local/bin/ && \  
ln -s /usr/local/pipeline/kraken/kraken-translate /usr/local/bin/ && \  
chmod -R 755 /usr/local/pipeline/kraken && \  
chown -R snappy:snappy /usr/local/pipeline && \  
rm -rvf /tmp/*  
  
CMD ["/bin/bash"]  

