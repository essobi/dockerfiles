# use latest Node image  
FROM maven:3-jdk-7  
# install Fabric  
RUN apt-get -y update  
RUN apt-get -y install build-essential libssl-dev libffi-dev  
RUN apt-get -y install python2.7 python-pip python-dev build-essential  
RUN pip install --upgrade cffi # to fix this
https://github.com/byt3bl33d3r/MITMf/issues/163  
RUN pip install fabric  
  
# install gcloud  
RUN apt-get -y install apt-utils lsb-release  
RUN apt-get -y install apt-transport-https  
RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c
-s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list  
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -  
RUN apt-get -y update  
RUN apt-get -y install google-cloud-sdk=142.0.0-0

