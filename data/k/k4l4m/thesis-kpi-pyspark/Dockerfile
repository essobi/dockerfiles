FROM k4l4m/spark-base:2.1.0-hadoop2.7  
ENV SPARK_MASTER=spark://spark-master:7077  
ENV EXECUTOR_MEMORY=10G  
ENV SPARK_JOB=src/main.py  
  
RUN apt-get update && apt-get -y install zip  
  
RUN mkdir -p /usr/src/app  
  
COPY src /usr/src/app/src  
COPY mysql-connector-java-5.1.40-bin.jar /usr/src/app  
COPY prepare-deps.sh /usr/src/app  
COPY submit-cluster.sh /usr/src/app  
  
WORKDIR /usr/src/app  
  
RUN pip3 install -t dependencies requests  
RUN ./prepare-deps.sh  
  
CMD ./submit-cluster.sh $SPARK_MASTER $EXECUTOR_MEMORY $SPARK_JOB  
  

