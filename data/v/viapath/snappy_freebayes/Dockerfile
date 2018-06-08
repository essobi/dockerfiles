FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
  
## freebayes (and bamtools)  
RUN cd /tmp && \  
git clone \--recursive https://github.com/ekg/freebayes.git && \  
cd freebayes && \  
git checkout c15a283630ed938ce0cc09548a94c764faa09ac5 && \  
git submodule update --recursive && \  
make && \  
mkdir -p /usr/local/pipeline/freebayes/bamtools && \  
mv bin /usr/local/pipeline/freebayes && \  
mv scripts /usr/local/pipeline/freebayes && \  
mv bamtools/bin /usr/local/pipeline/freebayes/bamtools && \  
ln -s /usr/local/pipeline/freebayes/bin/freebayes /usr/local/bin && \  
ln -s /usr/local/pipeline/freebayes/bamtools/bin/bamtools /usr/local/bin && \  
chmod -R 755 /usr/local/pipeline/freebayes && \  
chown -R snappy:snappy /usr/local/pipeline && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/freebayes/bin' /home/snappy/.bashrc
&& \  
rm -rf /tmp/freebayes  
  
CMD ["/bin/bash"]  

