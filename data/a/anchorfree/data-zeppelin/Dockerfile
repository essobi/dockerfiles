FROM anchorfree/data-base:2.1  
USER root  
  
ENV SPARK_HIVE true  
ENV ZEPPELIN_HOME /zeppelin  
  
RUN ln -s /usr/lib/jvm/java-8-oracle /usr/lib/jvm/default-java  
  
RUN R -e "install.packages('devtools', repos =
'http://cran.us.r-project.org')"  
RUN R -e "install.packages('knitr', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('ggplot2', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('rJava', repos = 'http://cran.us.r-project.org')"  
RUN R -e "install.packages('RJDBC', repos = 'http://cran.us.r-project.org')"  
RUN apt-get update && apt-get install -y python-numpy python-scipy python-
matplotlib ipython ipython-notebook python-pandas python-sympy python-nose  
  
COPY events_per_user /events_per_user  
  
WORKDIR /events_per_user  
RUN mvn clean install  
  
RUN git clone \--depth 1 --branch branch-0.7
https://epahomov:lk32lk32@github.com/AnchorFree/zeppelin.git /zeppelin  
  
RUN cd /zeppelin && \  
echo "tail -F /zeppelin/logs/*" >> bin/zeppelin-daemon.sh && \  
./dev/change_scala_version.sh 2.11 && \  
echo '{ "allow_root": true }' >> /root/.bowerrc && \  
apt-get install -y npm && \  
mvn clean package -Pspark-2.1 -Pscala-2.11 -Phadoop-2.7 -Psparkr -Pyarn
-Ppyspark -DskipTests -Pvendor-repo && \  
chmod -R 777 /zeppelin && \  
chown -R egor /zeppelin  
  
COPY zeppelin-configs /zeppelin-configs  
  
RUN mv /zeppelin-configs/* /zeppelin/conf && \  
chmod -R 777 /zeppelin/conf/* && \  
chown -R egor /zeppelin/conf/*  
  
USER egor  
  
ENV ZEPPELIN_PORT=35430  
CMD ["/zeppelin/bin/zeppelin-daemon.sh","start"]

