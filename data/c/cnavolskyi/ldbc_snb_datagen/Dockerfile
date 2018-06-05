FROM ubuntu  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/jre  
ENV HADOOP_HOME /app/hadoop-2.6.0  
ENV LDBC_SNB_DATAGEN_HOME /app/ldbc_snb_datagen  
  
ENV NUM_PERSONS 10000  
ENV NUM_YEARS 3  
ENV START_YEAR 2010  
ENV COMPRESSED false  
ENV UPDATE_STREAM false  
ENV NUM_THREADS 1  
ENV PERSON_SERIALIZER
ldbc.snb.datagen.serializer.snb.interactive.CSVPersonSerializer  
ENV INVARIANT_SERIALIZER
ldbc.snb.datagen.serializer.snb.interactive.CSVInvariantSerializer  
ENV PERSON_ACTIVITY_SERIALIZER
ldbc.snb.datagen.serializer.snb.interactive.CSVPersonActivitySerializer  
  
WORKDIR /app  
  
COPY . ldbc_snb_datagen  
  
RUN apt-get update  
RUN apt-get install -y $(cat ldbc_snb_datagen/dependencies.txt)  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN yes | apt-get install -y oracle-java8-installer  
RUN wget -O hadoop
"http://archive.apache.org/dist/hadoop/core/hadoop-2.6.0/hadoop-2.6.0.tar.gz"  
RUN tar -xzf hadoop  
RUN rm -rf hadoop  
RUN apt-get clean  
  
WORKDIR /app/ldbc_snb_datagen  
  
CMD ["bash", "run.sh"]

