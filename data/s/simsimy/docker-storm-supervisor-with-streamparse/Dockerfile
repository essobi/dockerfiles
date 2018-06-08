FROM openjdk:8-jdk  
USER root  
  
RUN apt-get update && apt-get install -y python  
RUN apt-get update && apt-get install -y python-dev  
RUN apt-get update && apt-get install -y libpq-dev  
RUN apt-get update && apt-get install -y libsnappy-dev  
RUN apt-get update && apt-get install -y python-pip  
RUN apt-get update && apt-get install -y libffi-dev  
  
RUN pip install -U pip  
RUN pip install -U cffi  
RUN pip install -U streamparse  
RUN pip install -U virtualenv  
  
ENV STORM_USER=storm \  
STORM_CONF_DIR=/conf \  
STORM_DATA_DIR=/data \  
STORM_LOG_DIR=/logs \  
STORM_VERSION=1.0.2  
  
RUN set -x \  
&& useradd -m "$STORM_USER" \  
&& mkdir -p "$STORM_CONF_DIR" "$STORM_DATA_DIR" "$STORM_LOG_DIR" \  
&& chown -R "$STORM_USER:$STORM_USER" "$STORM_CONF_DIR" "$STORM_DATA_DIR"
"$STORM_LOG_DIR"  
RUN set -x && wget -q "http://www.apache.org/dist/storm/apache-
storm-$STORM_VERSION/apache-storm-$STORM_VERSION.tar.gz"  
RUN set -x && tar -xzf "apache-storm-$STORM_VERSION.tar.gz"  
RUN set -x && chown -R "$STORM_USER:$STORM_USER" "apache-storm-$STORM_VERSION"  
RUN set -x && rm -r "apache-storm-$STORM_VERSION.tar.gz"  
  
  
WORKDIR apache-storm-$STORM_VERSION  
  
ENV PATH $PATH:/apache-storm-$STORM_VERSION/bin  
COPY docker-entrypoint.sh /  
COPY sync-venv.sh /  
RUN chmod +x /docker-entrypoint.sh  
RUN chmod +x /sync-venv.sh  
  
VOLUME ["/topologies"]  
VOLUME ["/env_specs"]  
VOLUME ["/stream_parse_logs"]  
ENTRYPOINT ["/docker-entrypoint.sh"]  

