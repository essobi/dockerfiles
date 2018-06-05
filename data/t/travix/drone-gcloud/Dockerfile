FROM travix/base-debian:latest  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV LEGO_VERSION=0.3.1  
ENV GCLOUD_VERSION=163.0.0  
ENV PATH="/opt/lego:/var/go/google-cloud-sdk/bin:${PATH}"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
ssh \  
python-openssl \  
jq \  
libxml2-utils \  
xmlstarlet \  
xz-utils \  
python \  
python-setuptools \  
gettext \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -fSL
"https://github.com/ejwa/gitinspector/releases/download/v0.4.4/gitinspector_0.4.4-1_all.deb"
-o gitinspector.deb \  
&& dpkg -i gitinspector.deb \  
&& rm -rf gitinspector.deb  
  
RUN mkdir /var/go \  
&& mkdir -p /opt/lego  
  
# copy the lego binary into the image  
COPY lego /opt/lego  
  
RUN chmod 777 /opt/lego/lego  
  
WORKDIR /var/go  
  
RUN curl -fSL
"https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz" -o google-cloud-sdk-linux.tar.gz \  
&& tar -xf google-cloud-sdk-linux.tar.gz -C /var/go \  
&& rm -rf google-cloud-sdk-linux.tar.gz \  
&& /var/go/google-cloud-sdk/install.sh \  
&& /var/go/google-cloud-sdk/bin/gcloud config set disable_usage_reporting true
\  
&& /var/go/google-cloud-sdk/bin/gcloud components install alpha -q \  
&& /var/go/google-cloud-sdk/bin/gcloud components install beta -q \  
&& /var/go/google-cloud-sdk/bin/gcloud components install kubectl -q \  
&& /var/go/google-cloud-sdk/bin/gcloud config set --installation
component_manager/disable_update_check true  
# runtime environment variables  
ENV CLOUDSDK_PYTHON_SITEPACKAGES "1"  

