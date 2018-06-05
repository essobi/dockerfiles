FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
# python dependencies  
RUN pip install -U numpy scipy scikit-learn argparse  
  
# # WHAM 1.7.0 (dependencies not met!)  
# RUN mkdir -p /usr/local/pipeline/ && \  
# wget --no-verbose -O /usr/local/pipeline/wham-1.7.0.tar.gz
https://github.com/zeeev/wham/archive/v1.7.0.tar.gz && \  
# tar xvfz wham-1.7.0.tar.gz && \  
# rm -f wham-1.7.0.tar.gz && \  
# cd /usr/local/pipeline/wham-1.7.0 && \  
# make && \  
# chmod -R 755 /usr/local/pipeline/wham-1.7.0 && \  
# chown -R snappy:snappy /usr/local/pipeline && \  
# ln -s /usr/local/pipeline/wham-1.7.0 /usr/local/bin/ && \  
# sed -i '$aPATH=$PATH:/usr/local/pipeline/wham-1.7.0' /home/snappy/.bashrc  
# WHAM from source  
RUN mkdir -p /usr/local/pipeline/ && cd /usr/local/pipeline/ && \  
git clone \--recursive https://github.com/zeeev/wham.git && \  
cd /usr/local/pipeline/wham && make && \  
chmod -R 755 /usr/local/pipeline/wham && \  
chown -R snappy:snappy /usr/local/pipeline && \  
ln -s /usr/local/pipeline/wham/bin/WHAM-GRAPHENING /usr/local/bin/ && \  
ln -s /usr/local/pipeline/wham/bin/WHAM-BAM /usr/local/bin/ && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/wham/bin' /home/snappy/.bashrc  
  
CMD ["/bin/bash"]  

