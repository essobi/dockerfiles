FROM oxbrcinformatics/java:jre8  
MAINTAINER Oliver Freeman <oliver.freeman@ndm.ox.ac.uk>  
  
ENV PATH=/java/bin:$PATH \  
FILE_RECEIVER_VERSION=1.0.9\  
RABBITMQ_HOST=rabbitmq \  
RABBITMQ_PORT=5672  
LABEL vendor="Oxford BRC Informatics" \  
version=${FILE_RECEIVER_VERSION}  
  
RUN apk add --update curl && \  
curl -LO
https://bintray.com/artifact/download/oxbrcinformatics/maven/ox/softeng/gel/file-
receiver/${FILE_RECEIVER_VERSION}/\  
file-receiver-${FILE_RECEIVER_VERSION}.tar && \  
tar xf file-receiver-${FILE_RECEIVER_VERSION}.tar && \  
cp -R file-receiver-${FILE_RECEIVER_VERSION}/bin . && \  
cp -R file-receiver-${FILE_RECEIVER_VERSION}/lib . && \  
rm -rf file-receiver-${FILE_RECEIVER_VERSION} && \  
rm file-receiver-${FILE_RECEIVER_VERSION}.tar && \  
mkdir config  
  
COPY ./bin ./bin  
  
# This allows for development by copying anything from the gradle installDist
command into the container  
# When releasing make sure the install dir is empty of all files bar the
.gitignore files.  
COPY ./install .  
  
RUN chmod +x /java/bin/*  
  
ENTRYPOINT ["wait-for-rabbitmq.sh", "file-receiver"]  
CMD ["-h"]

