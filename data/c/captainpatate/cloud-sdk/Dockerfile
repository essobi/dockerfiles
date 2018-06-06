FROM alpine:latest  
  
RUN \  
apk add -U \  
bash \  
ca-certificates \  
curl \  
python \  
py-crypto \  
py-django \  
py-jinja2 \  
py-lxml \  
py-libxslt \  
py2-pip \  
py-pillow \  
py-xml  
  
ENV HOME /  
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1  
RUN curl -s -o -
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-139.0.1-linux-x86_64.tar.gz | tar xzf -  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --additional-components app-
engine-python beta  
  
# Disable updater check for the whole installation.  
# Users won't be bugged with notifications to update to the latest version of
gcloud.  
RUN google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true  
  
# Disable updater completely.  
# Running `gcloud components update` doesn't really do anything in a union FS.  
# Changes are lost on a subsequent run.  
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/google-cloud-sdk/lib/googlecloudsdk/core/config.json  
  
# Workaround for
https://code.google.com/p/googleappengine/issues/detail?id=13477  
RUN curl -s -o /google-cloud-
sdk/platform/google_appengine/lib/cacerts/urlfetch_cacerts.txt
https://curl.haxx.se/ca/cacert.pem  
  
RUN mkdir /.ssh  
ENV PATH /google-cloud-sdk/bin:$PATH  
VOLUME ["/.config"]  
CMD ["/bin/bash"]  
  
ENV APPENGINE=/usr/local/google-cloud-sdk/bin  
RUN pip install webob webapp2  
  
WORKDIR /app  
EXPOSE 8000  
EXPOSE 8080  
CMD ["/bin/bash"]

