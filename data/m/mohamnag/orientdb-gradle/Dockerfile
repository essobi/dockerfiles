FROM mohamnag/orientdb  
MAINTAINER Mohammad Naghavi <mohamnag@gmail.com>  
  
ADD https://services.gradle.org/distributions/gradle-2.4-all.zip
/usr/bin/gradle-2.4-all.zip  
  
WORKDIR /usr/bin  
RUN apt-get install -y unzip  
RUN unzip gradle-2.4-all.zip && \  
ln -s gradle-2.4 gradle && \  
rm gradle-2.4-all.zip  
  
ENV GRADLE_USER_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_USER_HOME/bin  

