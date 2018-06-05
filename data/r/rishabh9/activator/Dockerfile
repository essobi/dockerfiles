FROM openjdk:8-jdk-alpine  
MAINTAINER Rishabh Joshi <rishabh9@gmail.com>  
  
ENV ACTIVATOR_VERSION 1.3.12  
RUN apk update && apk add bash wget unzip  
  
WORKDIR /opt  
  
RUN wget -q --progress=dot:mega http://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip \  
&& unzip -qq typesafe-activator-$ACTIVATOR_VERSION.zip \  
&& mv activator-dist-$ACTIVATOR_VERSION /opt/activator \  
&& ln -s /opt/activator/bin/activator /usr/local/bin/activator \  
&& rm -f typesafe-activator-$ACTIVATOR_VERSION.zip  
  
RUN mkdir /home/app  
ADD . /home/app  
WORKDIR /home/app  
  
EXPOSE 8888  
EXPOSE 9000  
EXPOSE 9999  
ENTRYPOINT ["activator", "-Dhttp.address=0.0.0.0"]  
  
# Default Command  
CMD ["ui"]  

