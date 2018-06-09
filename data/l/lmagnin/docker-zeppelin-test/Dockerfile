FROM epahomov/docker-zeppelin  
  
# ZEPPELIN  
ENV ZEPPELIN_HOME /incubator-zeppelin  
  
WORKDIR $ZEPPELIN_HOME  
  
#git checkout branch-0.5.6  
# master branch, as of March 31, 2016 / https://github.com/apache/incubator-
zeppelin/commit/0ee791ce29b2c72b6c662d5e1e154fb8dde8c60e  
# master branch, as of April 4, 2016 / https://github.com/apache/incubator-
zeppelin/commit/b51af33cb1e74f337ee119f8a26f87989d86fcbc  
RUN git pull; git reset --hard b51af33cb1e74f337ee119f8a26f87989d86fcbc;  
  
# To reduce the risk of "Untar re-exec error: exit status 1: output: write
/root/.npm/caniuse-db/1.0.30000446/package/fulldata-json/data-2.0.json: no
space left on device":  
#http://stackoverflow.com/questions/3119850/is-there-a-way-to-clean-up-git  
#RUN git clean -d -f;  
RUN git gc  
  
RUN mvn clean package -DskipTests -Pspark-1.6 -Dspark.version=1.6.1  
  
# TODO (?) Build [embedded] spark-cassandra-connector from Git
(https://github.com/datastax/spark-cassandra-
connector/blob/master/doc/12_building_and_artifacts.md)?  
#COPY ./conf $ZEPPELIN_HOME/provided-conf/  
#RUN ls $ZEPPELIN_HOME/provided-conf/  
COPY ./libs $ZEPPELIN_HOME/provided-libs/  
RUN ls $ZEPPELIN_HOME/provided-libs/  
  
COPY ./notebook $ZEPPELIN_HOME/provided-notebook/  
RUN ls $ZEPPELIN_HOME/provided-notebook/  
  
ENV ZEPPELIN_ALT /zeppelin  
RUN ln -s $ZEPPELIN_HOME $ZEPPELIN_ALT  
  
VOLUME $ZEPPELIN_ALT/data  
VOLUME $ZEPPELIN_ALT/notebook  
VOLUME $ZEPPELIN_ALT/libs  
#VOLUME $ZEPPELIN_ALT/conf  
#cp -r -u $ZEPPELIN_HOME/provided-conf/* $ZEPPELIN_HOME/conf/ ;  
CMD cp -r -u $ZEPPELIN_HOME/provided-notebook/* $ZEPPELIN_HOME/notebook/ ; cp
-r -u $ZEPPELIN_HOME/provided-libs/* $ZEPPELIN_HOME/libs/ ; ./bin/zeppelin.sh
start

