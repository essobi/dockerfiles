FROM viapath/snappy_ngstools:flatdog  
MAINTAINER David Brawand <dbrawand@nhs.net>  
ENV HOME /root  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
## varDictJava>=1.4.5  
RUN cd /usr/local/pipeline/ && \  
git clone \--recursive https://github.com/AstraZeneca-NGS/VarDictJava.git && \  
cd VarDictJava && \  
git checkout c96b0e56a00cd814120e1246a764f3e9ac655413 && \  
git submodule update --recursive  
  
RUN cd /usr/local/pipeline/VarDictJava && \  
./gradlew clean installApp && \  
chmod -R 755 /usr/local/pipeline/VarDictJava && \  
chown -R snappy:snappy /usr/local/pipeline && \  
sed -i '$aPATH=$PATH:/usr/local/pipeline/VarDictJava/VarDict'
/home/snappy/.bashrc  
  
# varDict  
RUN cd /usr/local/pipeline/ && \  
git clone \--recursive https://github.com/AstraZeneca-NGS/vardict.git && \  
cd vardict && \  
git checkout 149329ec5843b83df78b2ed9455e86145f54c9f7 && \  
git submodule update --recursive && \  
chmod -R 755 /usr/local/pipeline/vardict && \  
chown -R snappy:snappy /usr/local/pipeline  
  
ENV PATH /usr/local/pipeline/vardict:$PATH  
  
CMD ["/bin/bash"]  

