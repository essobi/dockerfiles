FROM alpine:3.6  
LABEL maintainer="Andrei Varabyeu <andrei_varabyeu@epam.com>"  
LABEL version=4.2.0  
  
ENV APP_DOWNLOAD_URL https://dl.bintray.com/epam/reportportal/4.2.0/service-
index_linux_amd64  
  
ADD ${APP_DOWNLOAD_URL} /service-index  
  
RUN chmod +x /service-index  
  
EXPOSE 8080  
ENTRYPOINT ["/service-index"]  

