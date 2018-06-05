FROM alpine:3.7  
LABEL maintainer="Andrei Varabyeu <andrei_varabyeu@epam.com>"  
LABEL version=4.2.0  
  
ENV APP_DOWNLOAD_URL https://dl.bintray.com/epam/reportportal/4.2.0  
ADD ${APP_DOWNLOAD_URL}/service-analyzer_linux_amd64 /service-analyzer  
  
RUN chmod +x /service-analyzer  
  
EXPOSE 8080  
ENTRYPOINT ["/service-analyzer"]  

