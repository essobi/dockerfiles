FROM n0ts/ubuntu-java  
  
MAINTAINER Naoya Nakazawa <naoya.n@gmail.com>  
  
ENV DYNAMODB_LOCAL_DIR=/opt/dynamodb-local  
ENV JAVA_OPTS "$JAVA_OPTS"  
RUN set -x \  
&& curl -L -o /opt/dynamodb_local.tar.gz \  
https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz
\  
&& mkdir -p $DYNAMODB_LOCAL_DIR \  
&& tar xvzf /opt/dynamodb_local.tar.gz -C $DYNAMODB_LOCAL_DIR  
  
COPY run.sh /opt/dynamodb-local/run.sh  
  
ENTRYPOINT ["/opt/dynamodb-local/run.sh"]  
  
CMD ["-help"]  

