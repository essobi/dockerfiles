FROM buildbot/buildbot-worker:latest  
MAINTAINER Oscar Prieto <oscarmpp@gmail.com>  
  
USER root  
  
# Set the locale  
RUN apt-get clean && apt-get update && apt-get install -y locales tzdata  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# Install the packages  
RUN pip --no-cache-dir install -U \  
selenium \  
unidecode \  
robotframework \  
requests \  
influxdb \  
robotframework-appiumlibrary \  
robotframework-browsermobproxylibrary \  
robotframework-requests  
  
# needed until the final SeleniumLibrary 3.0 is released  
RUN pip --no-cache-dir install --pre --upgrade robotframework-seleniumlibrary  

