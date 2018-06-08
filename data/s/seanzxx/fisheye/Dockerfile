FROM java:8-jre  
  
MAINTAINER Sean Zeng<seanzxx@me.com>  
  
ENV FISHEYE_HOME /opt/fisheye  
ENV FISHEYE_VERSION 4.2.1  
ENV FISHEYE_WORK /fisheye-work  
ENV FISHEYE_INST $FISHEYE_WORK  
  
ADD
https://www.atlassian.com/software/fisheye/downloads/binary/fisheye-$FISHEYE_VERSION.zip
/tmp  
RUN mkdir -p /opt && \  
unzip /tmp/fisheye-$FISHEYE_VERSION.zip -d /opt && \  
mv /opt/fecru-$FISHEYE_VERSION /opt/fisheye-$FISHEYE_VERSION && \  
ln -s /opt/fisheye-$FISHEYE_VERSION $FISHEYE_HOME && \  
rm -f /tmp/fisheye-$FISHEYE_VERSION.zip  
  
RUN useradd -r -u 300 -m -c "fisheye role account" -d $FISHEYE_WORK -s
/bin/false fisheye  
  
EXPOSE 8060  
USER fisheye  
  
WORKDIR $FISHEYE_HOME  
  
CMD bin/fisheyectl.sh run  
  

