ARG PYTHON_VERSION=3  
FROM godatadriven/miniconda:${PYTHON_VERSION}  
  
ENV PYTHONDONTWRITEBYTECODE 1  
ARG BUILD_DATE  
ARG AIRFLOW_VERSION  
ARG
AIRFLOW_EXTRAS=async,celery,crypto,jdbc,hdfs,hive,azure,gcp_api,emr,password,postgres,slack,ssh  
  
LABEL org.label-schema.name="Apache Airflow ${AIRFLOW_VERSION}" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$AIRFLOW_VERSION  
  
RUN apt-get update \  
&& apt-get install -y gcc g++ netcat git ca-certificates --no-install-
recommends \  
&& if [ "$AIRFLOW_VERSION" = "master" ]; then\  
pip install --no-cache-dir git+https://github.com/apache/incubator-
airflow/#egg=apache-airflow[$AIRFLOW_EXTRAS];\  
elif [ -n "$AIRFLOW_VERSION" ]; then\  
pip install --no-cache-dir apache-airflow[$AIRFLOW_EXTRAS]==$AIRFLOW_VERSION;\  
else\  
pip install --no-cache-dir apache-airflow[$AIRFLOW_EXTRAS];\  
fi\  
&& apt-get remove -y --purge gcc g++ git\  
&& apt-get clean -y  
  
COPY entrypoint.sh /scripts/  
RUN chmod +x /scripts/entrypoint.sh  
  
WORKDIR /usr/local/airflow  
VOLUME ["/usr/local/airflow/dags", "/usr/local/airflow/logs"]  
  
ENTRYPOINT ["/scripts/entrypoint.sh"]  
CMD ["--help"]

