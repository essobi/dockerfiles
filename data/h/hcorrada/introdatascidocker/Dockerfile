FROM rocker/ropensci  
MAINTAINER Hector Corrada Bravo <hcorrada@gmail.com>  
  
  
# install Spark  
WORKDIR /home/root  
RUN wget
http://mirror.cogentco.com/pub/apache/spark/spark-1.2.1/spark-1.2.1.tgz  
RUN tar zxvf spark-1.2.1.tgz  
WORKDIR /home/root/spark-1.2.1  
RUN sbt/sbt assembly  
  
# install sparkR  
ADD installSpark.r /tmp/installSpark.r  
RUN Rscript /tmp/installSpark.r  
  
# install datasets from ISL  
RUN install2.r --error \  
ISLR \  
gapminder \  
cvTools \  
tree \  
e1071 \  
ROCR \  
randomForest  
  
# install hadley's excel reader package  
RUN installGithub.r \  
hadley/readxl  
  

