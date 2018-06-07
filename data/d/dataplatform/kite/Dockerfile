FROM dataplatform/hadoop:0.1.0  
MAINTAINER tpham  
  
WORKDIR /tools  
  
COPY avro_schema_infer.sh /tools  
RUN chmod +x /tools/avro_schema_infer.sh  
  
RUN curl http://central.maven.org/maven2/org/kitesdk/kite-tools/1.0.0/kite-
tools-1.0.0-binary.jar -o kite-dataset  
RUN chmod +x kite-dataset  
  
RUN yum install -y php  
RUN yum install -y php-cli.x86_64

