FROM jupyter/all-spark-notebook  
  
USER root  
  
RUN mkdir -p /usr/lib/yelp_data/  
COPY ./processor/target/scala-2.11/yelp-data-processor-
assembly-0.0.1-SNAPSHOT.jar /usr/lib/yelp_data/  
  
RUN mkdir -p /usr/lib/yelp_data/stopwords  
COPY ./processor/src/main/resources/data/stopwords/
/usr/lib/yelp_data/stopwords/  
  
RUN mkdir -p /root/pipeline/  
  
RUN mkdir -p /root/pipeline  
COPY ./pipeline/ /root/pipeline/  
RUN ls /root/pipeline/  
RUN mkdir -p /root/pipeline/logs  
  
RUN conda install virtualenv -y  
RUN cd /root/pipeline && virtualenv venv --python=python2.7  
  
RUN bash -c "source /root/pipeline/venv/bin/activate && pip install -r
/root/pipeline/etc/requirements/prod.txt"  
RUN echo "source /root/pipeline/venv/bin/activate" >> ~/.bashrc  
  
ENV LUIGI_CONFIG_PATH /root/pipeline/etc/conf/luigi.cfg  
  
ENV PATH ${PATH}:${SPARK_HOME}/bin  
  
ENV DYNACONF_SETTINGS settings.prod  
  
ENV SPARK_OPTS='--master local --conf
spark.cassandra.connection.host=cassandra --packages com.datastax.spark:spark-
cassandra-connector_2.11:2.0.3'  
# Moving prepared notebooks to serve them  
COPY ./notebooks/ /home/jovyan/

