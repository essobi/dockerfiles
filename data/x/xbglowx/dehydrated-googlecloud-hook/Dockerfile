FROM xbglowx/dehydrated:latest  
LABEL maintainer="Brian Glogower <xbglowx@gmail.com>"  
  
ENV PATH=/dehydrated/google-cloud-sdk/bin:$PATH  
WORKDIR /dehydrated  
RUN mkdir -p hooks && \  
git clone https://github.com/spfguru/dehydrated4googlecloud.git hooks/google-
cloud  
RUN apk --no-cache add bind-tools python && \  
curl -L https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-
sdk.tar.gz | \  
tar -xzvf- && \  
google-cloud-sdk/install.sh -q  
  
ENTRYPOINT ["./dehydrated"]  
CMD ['-h']  

