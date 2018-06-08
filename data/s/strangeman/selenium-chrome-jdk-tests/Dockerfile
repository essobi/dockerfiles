FROM selenium/standalone-chrome:latest  
MAINTAINER Anton Markelov <doublic@gmail.com>  
  
USER root  
  
# Install openjdk-8-jdk-headless  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
openjdk-8-jdk-headless libnss3 libgconf-2-4 \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# USER seluser  
ENV DISPLAY :99  
ENV TZ=Europe/Moscow  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
CMD /run.sh  

