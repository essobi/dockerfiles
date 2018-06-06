FROM crazycode/jdk8  
  
MAINTAINER crazycode  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y unzip wget  
  
RUN cd /tmp && wget http://downloads.typesafe.com/typesafe-
activator/1.2.10/typesafe-activator-1.2.10.zip  
RUN cd /tmp && unzip -q typesafe-activator-1.2.10.zip && rm -f typesafe-
activator-1.2.10.zip  
RUN mv /tmp/activator-1.2.10 /opt/  
RUN ln -s /opt/activator-1.2.10/activator /usr/local/bin/  
  
# Create dummy project to download artifacts.  
RUN cd /tmp \  
&& activator new testscala play-scala  
  
RUN cd /tmp/testscala \  
&& activator compile \  
&& activator test  
  
RUN cd /tmp \  
&& activator new testjava play-java  
  
RUN cd /tmp/testjava \  
&& activator compile \  
&& activator test  
  
RUN rm -rf /tmp/test*  
  
RUN chmod +x /opt/activator-1.2.10/activator  
  
EXPOSE 9000  
ADD profile /profile  
  
CMD ["/bin/bash", "--rcfile", "/profile", "-i"]  

