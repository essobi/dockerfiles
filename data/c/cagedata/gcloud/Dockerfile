FROM alpine:latest  
  
ENV GOOGLE_CLOUD_SDK_VERSION 144.0.0  
RUN apk --update add openssl openssl-dev gcc python python-dev py-pip musl-dev
libffi-dev ca-certificates  
RUN pip install --quiet pyopenssl  
  
ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${GOOGLE_CLOUD_SDK_VERSION}-linux-x86_64.tar.gz /opt/google-cloud-
sdk.tar.gz  
RUN tar -xzf /opt/google-cloud-sdk.tar.gz -C /opt && \  
/opt/google-cloud-sdk/install.sh --quiet --path-update=true \--command-
completion=true \  
\--usage-reporting=true \--additional-components kubectl beta  
  
ENV PATH /opt/google-cloud-sdk/bin:$PATH  
  
COPY docker-entrypoint.sh /opt/google-cloud-sdk/docker-entrypoint.sh  
  
ENTRYPOINT ["/opt/google-cloud-sdk/docker-entrypoint.sh"]  
  
CMD ["gcloud", "info"]  

