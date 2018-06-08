FROM hyperledger/fabric-baseimage:x86_64-0.4.6  
# install java and ant  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer ant  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/  
# setup hlf bftsmart  
ENV LOCAL_HLF_INSTALL $GOPATH/src/github.com/hyperledger/fabric  
COPY hyperledger-bftsmart.tar.gz $LOCAL_HLF_INSTALL/  
RUN cd $LOCAL_HLF_INSTALL && mkdir hyperledger-bftsmart && tar -xzf
hyperledger-bftsmart.tar.gz hyperledger-bftsmart -C hyperledger-bftsmart && rm
-f hyperledger-bftsmart.tar.gz  
RUN cd $LOCAL_HLF_INSTALL/hyperledger-bftsmart && ant  

