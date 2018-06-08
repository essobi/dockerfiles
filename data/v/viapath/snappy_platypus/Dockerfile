FROM viapath/snappy_base:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
## htslib  
RUN cd /tmp && \  
git clone git://github.com/samtools/htslib.git && \  
cd htslib && git checkout 1.2.1 && \  
make install && \  
rm -rf /tmp/*  
  
## Platypus (0.8.x?)  
RUN cd /usr/local/pipeline && \  
git clone \--recursive https://github.com/andyrimmer/Platypus.git && \  
cd /usr/local/pipeline/Platypus && git checkout
cb20846e4e508dbc5529423a860b2ff8b7630584 && \  
make && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/Platypus/bin' /home/snappy/.bashrc &&
\  
chown -R snappy:snappy /usr/local/pipeline && \  
chmod -R 755 /usr/local/pipeline/Platypus/bin && \  
rm -rf /usr/local/pipeline/Platypus/.git  
  
ENV C_INCLUDE_PATH /usr/local/include  
ENV LIBRARY_PATH /usr/local/lib  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
CMD ["/bin/bash"]  

