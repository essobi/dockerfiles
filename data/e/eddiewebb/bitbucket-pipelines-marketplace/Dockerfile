FROM openjdk:8-jdk  
  
MAINTAINER Edward A. Webb <ollitech@gmail.com>  
  
# install altassian SDK  
ADD http://sdkrepo.atlassian.com/deb-archive/atlassian-plugin-
sdk_6.2.14_all.deb /amps.deb  
RUN echo "deb http://sdkrepo.atlassian.com/debian/ stable contrib"
>>/etc/apt/sources.list \  
&& dpkg -i /amps.deb  
  
# add any dependency libraries in working repo  
COPY libs /debian_libs  
RUN dpkg -i /debian_libs/*.deb  
  
# Add our custom shipit scripts  
COPY pipelines /root/pipelines  
ENV PIPES_HOME /root/pipelines  
ENV PATH $PIPES_HOME:$PATH  
RUN ln -s $PIPES_HOME/shipit.sh /usr/bin/shipit  
  
# arg let's us pass in a value during build  
ARG GITHASH  
# but needs to be set as ENV variable too  
ENV GITHASH=$GITHASH

