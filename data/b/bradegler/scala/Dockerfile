FROM bradegler/gradle  
MAINTAINER Brad Egler "begler@gmail.com"  
  
WORKDIR /tmp  
RUN wget http://downloads.typesafe.com/typesafe-activator/1.2.12/typesafe-
activator-1.2.12.zip && \  
unzip typesafe-activator-1.2.12.zip && \  
rm typesafe-activator-1.2.12.zip && \  
mv activator-1.2.12 /usr/local/lib && \  
ln -s /usr/local/lib/activator-1.2.12/activator /usr/local/bin/activator  
  
RUN wget http://downloads.typesafe.com/scala/2.11.5/scala-2.11.5.tgz && \  
tar xvzf scala-2.11.5.tgz && \  
rm scala-2.11.5.tgz && \  
mv scala-2.11.5 /usr/local/lib/  
  
RUN wget https://dl.bintray.com/sbt/debian/sbt-0.13.7.deb && \  
dpkg -i sbt-0.13.7.deb && \  
rm sbt-0.13.7.deb  
  
VOLUME /data  
WORKDIR /data  
  
# Default activator server port  
EXPOSE 9000  
  
CMD ["/bin/bash"]  

