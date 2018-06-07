FROM sbubmi/pathomics_analysis:latest  
  
RUN yum makecache fast  
  
RUN yum -y install curl-devel jsoncpp-devel libev-devel && \  
ln -s /usr/include/jsoncpp/json /usr/include/json  
  
WORKDIR /tmp/  
  
RUN git clone https://github.com/redis/hiredis.git && \  
cd hiredis && make -j4 && make install  
  
WORKDIR /tmp/  
  
RUN git clone https://github.com/hmartiro/redox.git && \  
cd redox && \  
mkdir build && cd build && \  
cmake ../ && \  
make -j4 && make install  
  
WORKDIR /tmp/  
  
RUN git clone -b release https://github.com/camicroscope/DynamicServices.git
&& \  
cd DynamicServices/ && \  
mkdir images && \  
mkdir configs && \  
mkdir obj && make -j4  
  
WORKDIR /tmp/DynamicServices/  
  
COPY trusted-app-client-0.0.1-jar-with-dependencies.jar /tmp/DynamicServices/  
COPY trusted-app-client-0.0.1-jar-with-dependencies2.jar /tmp/DynamicServices/  
  
COPY createUser.py /tmp/DynamicServices/  
  
RUN yum -y install java-1.7.0-openjdk  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
ENV PATH $JAVA_HOME/bin:$PATH  
  
  
ENV LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64:$LD_LIBRARY_PATH  
COPY sample_config.json /tmp/DynamicServices/configs/config.json  
COPY sample_apikey.json /tmp/DynamicServices/configs/sample_apikey.json  
  
CMD ["/bin/bash", "/tmp/DynamicServices/run.sh"]  

