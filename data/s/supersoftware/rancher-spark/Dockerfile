FROM java:8-jre  
  
# install aws-cli  
RUN apt-get update \  
&& apt-get -y install python python-pip \  
&& pip install awscli --upgrade --user  
  
# install spark  
RUN cd /tmp \  
&& curl -LO https://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-
hadoop2.7.tgz \  
&& tar zxf spark-2.1.1-bin-hadoop2.7.tgz \  
&& mv spark-2.1.1-bin-hadoop2.7 /app \  
&& rm spark-2.1.1-bin-hadoop2.7.tgz  
  
# environment  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre  
ENV PATH=/app/bin:/app/sbin:~/.local/bin:$PATH  
ENV AWS_ACCESS_KEY_ID=xxxxxxxxx  
ENV AWS_SECRET_ACCESS_KEY=xxxxxxxxx  
ENV AWS_DEFAULT_REGION=us-east-1  
ENV ENDPOINT_URL=http://lb.minio:9000  
ENV APP_PATH=s3://dist/spark-app-assembly.jar  
ENV ASSEMBLY_NAME=spark-app-assembly.jar  
WORKDIR /app  
  
# entry point  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["idle"]  

