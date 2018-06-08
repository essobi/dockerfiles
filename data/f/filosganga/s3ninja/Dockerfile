FROM openjdk:8-alpine  
MAINTAINER Filippo De Luca <me@filippodeluca.com>  
  
ENV S3NINJA_VERSION 2.7  
ENV S3NINJA_DIR /s3ninja  
ENV S3NINJA_DATA_DIR ${S3NINJA_DIR}/data  
  
EXPOSE 9444  
VOLUME S3NINJA_DATA_DIR  
  
ADD
https://oss.sonatype.org/content/groups/public/com/scireum/s3ninja/${S3NINJA_VERSION}/s3ninja-${S3NINJA_VERSION}-zip.zip
/s3ninja-${S3NINJA_VERSION}-zip.zip  
RUN mkdir -p ${S3NINJA_DIR} && \  
unzip s3ninja-${S3NINJA_VERSION}-zip.zip -d ${S3NINJA_DIR} && \  
rm -f s3ninja-${S3NINJA_VERSION}-zip.zip && \  
mkdir -p ${S3NINJA_DATA_DIR}/objects && \  
mkdir -p ${S3NINJA_DATA_DIR}/multipart  
  
WORKDIR ${S3NINJA_DIR}  
  
COPY application.conf app/application.conf  
  
ENTRYPOINT ["java", "IPL"]  

