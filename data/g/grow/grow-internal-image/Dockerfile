FROM ubuntu:xenial  
MAINTAINER Grow Authors <hello@grow.io>  
  
# Update system.  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y --no-install-recommends software-properties-common  
  
# Set environment variables.  
ENV TERM=xterm  
  
# Set environment variables  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
# Node 8.  
RUN apt-get install -y --no-install-recommends curl ca-certificates  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# Golang.  
RUN add-apt-repository ppa:gophers/archive  
  
# gcloud tool.  
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key
add -  
  
# Install dependencies.  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends \  
python3 python3-pip python3-setuptools pylint nodejs build-essential zip libc6
libyaml-dev \  
libffi-dev libxml2-dev libxslt-dev libssl-dev git curl ssh google-cloud-sdk \  
google-cloud-sdk-app-engine-python golang-1.9-go  
  
# Add gcloud to path.  
ENV PYTHONPATH="${PYTHONPATH}:/usr/lib/google-cloud-
sdk/platform/google_appengine"  
# Add go to path.  
ENV PATH=$PATH:/usr/lib/go-1.9/bin  
ENV GOPATH=$HOME/gocode  
ENV PATH=$PATH:$GOPATH/bin  
  
# Update pip.  
RUN pip3 install --upgrade pip  
  
# Install Virtual Env  
RUN pip3 install virtualenv  
RUN pip3 install pipenv  
  
# Install NPM globals.  
RUN npm install -g gulp  
  
# Install github release uploader.  
RUN go get -u github.com/tcnksm/ghr  
  
# Clean up APT.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# Clean up Temp files.  
RUN rm -rf /tmp/* /var/tmp/*  
  
# Confirm versions that are installed.  
RUN python -v  
RUN pip3 --version  
RUN pipenv --version  
RUN node -v  
RUN gulp -v  
RUN gcloud -v  
RUN go version  
RUN ghr --version  

