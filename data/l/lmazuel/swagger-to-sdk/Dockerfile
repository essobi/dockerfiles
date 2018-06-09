FROM ubuntu:16.04  
USER root  
  
LABEL maintainer="lmazuel"  
  
# Basic Ubuntu packages + Ruby (libunwind for .NET)  
RUN apt-get update && apt-get install -y curl git software-properties-common
locales libunwind8 ruby bundler libpng-dev zlibc zlib1g zlib1g-dev  
  
# NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get update && apt-get install -y nodejs  
  
# Go 1.9  
RUN add-apt-repository ppa:gophers/archive && \  
apt-get update && \  
apt-get install -y golang-1.9-go  
ENV PATH="/usr/lib/go-1.9/bin:/root/go/bin:${PATH}"  
# Go dep  
RUN go get -u github.com/golang/dep/cmd/dep  
  
# Python 3.6 (as default Python)  
RUN add-apt-repository ppa:jonathonf/python-3.6 && \  
apt-get update && \  
apt-get install -y python3.6 && \  
ln -s /usr/bin/python3.6 /usr/local/bin/python  
  
# Install pip for Python 3.6  
RUN curl -sL https://bootstrap.pypa.io/get-pip.py | python3.6  
  
# Autorest  
WORKDIR /opt  
  
# pre-load dotnet framework runtime to slim down runtime effort  
RUN npm install dotnet-2.0.0  
  
# Autorest  
RUN npm install autorest@latest  
RUN ln -s /opt/node_modules/.bin/autorest /usr/local/bin  
  
# ensure autorest minimum version of the modeler  
RUN autorest --use="@microsoft.azure/autorest.modeler@2.0.21" \--allow-no-
input  
  
# Set the locale to UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
COPY setup.py /tmp  
COPY swaggertosdk /tmp/swaggertosdk/  
WORKDIR /tmp  
RUN pip3.6 install .[rest]  
  
WORKDIR /git-restapi  
ENTRYPOINT ["python3.6", "-m", "swaggertosdk"]  

