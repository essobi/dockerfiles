FROM java:latest  
RUN ["apt-get", "update"]  
RUN ["apt-get", "-y", "install", "python", "curl", "unzip"]  
RUN ["curl", "https:\/\/s3.amazonaws.com\/aws-cli\/awscli-bundle.zip", "-o",
"\/tmp\/awscli-bundle.zip"]  
RUN ["unzip", "\/tmp\/awscli-bundle.zip", "-d", "\/tmp"]  
RUN ["\/tmp\/awscli-bundle\/install", "-i", "\/usr\/local\/aws", "-b",
"\/usr\/local\/bin\/aws"]  
RUN ["rm", "\/tmp\/awscli-bundle.zip"]  
RUN ["rm", "-rf", "\/tmp\/awscli-bundle"]  
ENV JAVA_OPTS="-Xms1500m -Xmx1500m -Xss4m -XX:+HeapDumpOnOutOfMemoryError
-XX:+UseConcMarkSweepGC XX:+CMSParallelRemarkEnabled -XX:+ScavengeBeforeFullGC
-XX:+CMSScavengeBeforeRemark"  
ENV SECRET_BUCKET_NAME="driven-secrets"  
ENV DRIVEN_SERVER_VERSION="1.0.5"  
EXPOSE 8080  
EXPOSE 9090  
ADD /app/lib /app/lib  
ADD 238/driven_2.11-1.0.5.jar /app/driven_2.11-1.0.5.jar  
COPY 239/docker.conf app/docker.conf  
COPY 240/alpn-boot-8.1.7.v20160121.jar alpn-boot-8.1.7.v20160121.jar  
COPY 241/jetty-alpn-agent-2.0.2.jar jetty-alpn-agent-2.0.2.jar  
COPY 242/service-account.json app/service-account.json  
COPY 243/secrets-entrypoint.sh app/secrets-entrypoint.sh  
ENTRYPOINT ["\/app\/secrets-entrypoint.sh"]

