#####################################  
# Dockerfile for AggregatorDetector #  
# BigDataEurope #  
# #  
#####################################  
  
FROM gioargyr/adbase:1.0.1  
  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
# DOWNLOAD AND BUILD pre-processing stage (read-subset-calibrate-write)  
RUN git clone https://github.com/gioargyr/pilot-sc7-imgpreprocessor.git \  
&& cd /pilot-sc7-imgpreprocessor/pilot-sc7-imgpreprocessor \  
&& mvn clean package  
  
RUN mkdir /allApps \  
&& mkdir /allImages \  
&& mv /pilot-sc7-imgpreprocessor/pilot-sc7-imgpreprocessor/target/pilot-
sc7-imgpreprocessor-0.0.1-SNAPSHOT-allinone.jar /allApps/preprocessing.jar \  
&& rm -rf /pilot-sc7-imgpreprocessor  
  
  
# DOWNLOAD AND BUILD C++ TerrainCorrection code  
RUN git clone https://github.com/ArArgyridis/RangeDopplerTerrainCorrection.git
/RangeDopplerTerrainCorrection \  
&& cd /RangeDopplerTerrainCorrection \  
&& sed -i '/cmake/c\cmake -DCMAKE_C_COMPILER=/usr/bin/gcc-7
-DCMAKE_CXX_COMPILER=/usr/bin/g++-7 ../' build.sh \  
&& chmod +x build.sh \  
&& ./build.sh  
  
RUN mv /RangeDopplerTerrainCorrection/bin/RangeDopplerTerrainCorrection
/allApps  
  
  
# DOWNLOAD AND BUILD C++ ChangeDetection code  
RUN git clone https://github.com/ArArgyridis/LogRatioChangeDetection.git
/LogRatioChangeDetection \  
&& cd /LogRatioChangeDetection \  
&& sed -i '/cmake/c\cmake -DCMAKE_C_COMPILER=/usr/bin/gcc-7
-DCMAKE_CXX_COMPILER=/usr/bin/g++-7 ../' build.sh \  
&& chmod +x build.sh \  
&& ./build.sh  
  
RUN mv /LogRatioChangeDetection/bin/LogRatioChangeDetection /allApps  
  
  
# DOWNLOAD PyDBScan  
RUN git clone https://github.com/gioargyr/PyDBScan.git  
  
  
# DOWNLOAD AND BUILD image-aggregator service  
RUN git clone -b cycle3 https://github.com/big-data-europe/pilot-sc7-image-
aggregator.git \  
&& cd pilot-sc7-image-aggregator \  
&& mvn clean package  
  
RUN cp /pilot-sc7-image-aggregator/target/*.war /tomcat/webapps \  
&& rm -rf pilot-sc7-image-aggregator  
  
  
ADD downlDem.sh /downlDem.sh  
ADD runImgPreProcess.sh /runImgPreProcess.sh  
ADD runTerrainCorrection.sh /runTerrainCorrection.sh  
ADD runChangeDetection.sh /runChangeDetection.sh  
ADD runPyDBScan.sh /runPyDBScan.sh  
  
  
RUN chmod +x /*.sh  
  
EXPOSE $PORT  
CMD ["/bin/bash", "/runtomcat.sh"]  

