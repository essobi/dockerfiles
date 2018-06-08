FROM alpine:3.5  
ENV GOOGLE_APPLICATION_CREDENTIALS=/secret/google-auth.json  
  
RUN apk --update --no-cache add \  
bash \  
ca-certificates \  
wget \  
git \  
python  
  
WORKDIR /  
ARG GCLOUD_SDK_VERSION="152.0.0"  
ARG TERRAFORM_VERSION="0.9.5"  
RUN \  
FILENAME="google-cloud-sdk-${GCLOUD_SDK_VERSION}-linux-x86_64.tar.gz" && \  
wget "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/${FILENAME}"
&& \  
tar xf $FILENAME && \  
rm -rf $FILENAME && \  
FILENAME="terraform_${TERRAFORM_VERSION}_linux_amd64.zip" && \  
wget
"https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/${FILENAME}" &&
\  
unzip $FILENAME && \  
rm -rf $FILENAME && \  
mv terraform /usr/local/bin  
ENV PATH /google-cloud-sdk/bin:$PATH  
RUN \  
gcloud components update && \  
gcloud components install kubectl && \  
gcloud components install beta && \  
gcloud version && \  
terraform version  
  
COPY functions.sh setup.sh /usr/src/  
  
WORKDIR /usr/local/bin  
COPY apply.sh apply  
COPY create.sh create  
COPY replace.sh replace  
COPY plan.sh plan  
RUN chmod a+x apply create replace plan  
  
WORKDIR /deployment  
CMD apply  

