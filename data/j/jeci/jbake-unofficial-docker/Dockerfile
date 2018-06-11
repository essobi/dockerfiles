FROM maven:latest  
MAINTAINER Jeremie Lesage <info@jeci.fr>  
  
WORKDIR /root  
  
ENV JBAKE_VERSION 2.4.0.1  
ENV JBAKE_DATA "/data"  
RUN git clone -n https://github.com/jeci-sarl/jbake.git jbake \  
&& cd jbake \  
&& git checkout origin/v$JBAKE_VERSION  
WORKDIR /root/jbake  
  
RUN mvn package -Dmaven.test.skip=true \  
&& unzip /root/jbake/dist/jbake-$JBAKE_VERSION-bin.zip -d /opt \  
&& rm -rf /root/jbake/  
  
ENV JBAKE_HOME /opt/jbake-$JBAKE_VERSION/  
ENV PATH $JBAKE_HOME/bin:$PATH  
  
WORKDIR "$JBAKE_DATA"  
VOLUME "$JBAKE_DATA"  
EXPOSE 8820  
ENTRYPOINT ["jbake"]  
CMD ["-b -s"]  

