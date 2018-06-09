FROM alpine:3.6  
  
# Add gcloud, mongodb-tools  
# TODO: google-cloud-sdk will be available on Alpine soon  
RUN apk add \--no-cache --virtual .build-deps \  
curl \  
ca-certificates \  
tar \  
python-dev \  
py-pip \  
build-base && \  
mkdir -p /usr/src/google-cloud-sdk && \  
curl -sSL https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz |
tar xz -C /usr/src/google-cloud-sdk --strip-components 1 && \  
( \  
cd /usr/src/google-cloud-sdk && \  
./install.sh \--usage-reporting false --path-update true --quiet \  
) && \  
ln -s /usr/src/google-cloud-sdk/bin/* /usr/local/bin/. && \  
pip install --force -I crcmod && \  
apk --no-cache add \--virtual .rundeps \  
python \  
mongodb-tools && \  
apk del .build-deps  

