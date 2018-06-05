# Building a Play! app container based on Activator 1.3.2  
#  
# Thanks to https://registry.hub.docker.com/u/dordoka/play-framework/  
# for the main part of this Dockerfile  
#  
FROM jeanjerome/java-1.7.0-openjdk:1.0.0  
MAINTAINER Jean-Jerome Levy <contact@scalastic.io>  
  
# Install dependencies  
RUN yum install -y unzip sudo  
# This ones could be also helpful : git build-essential software-properties-
common  
# Create editor userspace  
RUN groupadd play  
RUN useradd play -m -g play -s /bin/bash  
# Very important ! play user must have userid set to 1000 for a working
activator  
RUN usermod -u 1000 play  
RUN passwd -l play  
RUN echo "play ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/play  
RUN chmod 0440 /etc/sudoers.d/play  
RUN mkdir -p /appli/play-app  
RUN chown play:play /appli/play-app  
  
WORKDIR /tmp  
RUN curl -O http://downloads.typesafe.com/typesafe-activator/1.3.2/typesafe-
activator-1.3.2.zip  
  
# Install play  
RUN unzip typesafe-activator-1.3.2.zip  
RUN rm -f typesafe-activator-1.3.2.zip  
RUN mv activator-1.3.2 /opt/activator  
RUN chown -R play:play /opt/activator  
  
# Remove unneeded dependencies  
RUN yum remove -y unzip && \  
yum clean all -y  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java  
RUN echo "export PATH=$PATH:/opt/activator" >> /home/play/.bashrc  
# Define user home. Activator will store ivy2 and sbt caches on /appli/play-
app volume  
RUN echo "export _JAVA_OPTIONS='-Duser.home=/appli/play-app'" >>
/home/play/.bashrc  
  
# Change user, launch bash  
USER play  
WORKDIR /home/play  
CMD ["/bin/bash"]  
  
# Expose play-app volume and play ports 9000 default  
VOLUME "/appli/play-app"  
EXPOSE 9000  
WORKDIR /appli/play-app

