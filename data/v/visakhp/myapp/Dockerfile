# Use latest ubuntu image as the base  
FROM ubuntu:17.10  
# add new user for this image  
RUN useradd -m visakh ; echo visakh: | chpasswd ; usermod -a -G root visakh  
  
# install repository  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties sudo  
  
# install java  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | sudo debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
  
# make sure that java installed successfully  
RUN java -version  
  
# create root directory  
RUN mkdir /springbootapp  
  
# copy the jar to root folder and allow permissions  
COPY spring*.jar /springbootapp  
RUN chmod -R 700 /springbootapp  
RUN chown -R visakh:root /springbootapp  
  
EXPOSE 8080  
WORKDIR /springbootapp  
  
ENV spring.h2.console.settings.web-allow-others=true  
CMD ["java", "-jar", "springbootapp.jar"]  

