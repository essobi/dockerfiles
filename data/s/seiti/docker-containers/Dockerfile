FROM java:7  
MAINTAINER Seiti Yamashiro <seiti@seiti.eti.br>  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ENV AWS_RDS_ROOT /opt/rds-tools  
ENV AWS_RDS_HOME $AWS_RDS_ROOT/tools  
ENV PATH $PATH:$AWS_RDS_HOME/bin  
# São Paulo is 'sa-east-1'  
ENV EC2_REGION sa-east-1  
# Export volume containing the secret file named aws-credential-file  
# i.e.: docker run --rm -v <dir_containing_file>:/.keys <docker image>  
ENV AWS_CREDENTIAL_FILE /.keys/aws-credential-file  
RUN mkdir /.keys  
ENV RDS_ZIP RDSCli.zip  
RUN mkdir -p $AWS_RDS_ROOT  
ADD http://s3.amazonaws.com/rds-downloads/$RDS_ZIP $AWS_RDS_ROOT/  
RUN unzip $AWS_RDS_ROOT/$RDS_ZIP -d $AWS_RDS_ROOT/ \  
&& rm -f $AWS_RDS_ROOT/$RDS_ZIP  
RUN ln -s $AWS_RDS_ROOT/`ls $AWS_RDS_ROOT` $AWS_RDS_HOME  
ENTRYPOINT ["rds"]  

