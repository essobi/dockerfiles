FROM alpine:3.6  
LABEL maintainer="Zadara Storage <support@zadarastorage.com>" \  
vendor="Zadara Storage"  
  
LABEL description="Squid proxy preconfigured with Object Storage Endpoints for
Zadara B2OS"  
  
RUN apk --no-cache add squid ca-certificates  
EXPOSE 3128  
ENV CUSTOM_MATCH=""  
COPY ./start.sh /start.sh  
COPY ./template /template  
  
CMD ["/start.sh"]  

