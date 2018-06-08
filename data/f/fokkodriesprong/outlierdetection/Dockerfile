FROM gettyimages/spark  
  
MAINTAINER Fokko Driesprong <fokko@driesprong.frl>  
  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key update  
RUN apt-get update  
RUN apt-get -y --force-yes install sbt  
  
ADD . /tmp/app  
WORKDIR /tmp/app  
  
RUN sbt compile  
RUN sbt assembly  
  
CMD /usr/spark/bin/spark-submit --class
com.quintor.EvaluateOutlierDetectionDistributed --master spark://master:7077
/tmp/app/target/scala-2.10/QuintorSparkOutlier-assembly-1.0.jar

