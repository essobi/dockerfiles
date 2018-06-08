FROM alpine:3.7  
LABEL maintainer="florian.lopes@outlook.com"  
  
ENV CONTAINER_STRUCTURE_TEST_DOWNLOAD_URL
https://storage.googleapis.com/container-structure-test/latest/container-
structure-test  
  
COPY entrypoint.sh /app/entrypoint.sh  
  
RUN chmod +x /app/entrypoint.sh  
  
VOLUME /test-config  
  
WORKDIR /test-config  
  
ENTRYPOINT ["/app/entrypoint.sh"]  
  
CMD ["--help"]  

