FROM shippableimages/ubuntu1404_java:0.0.1  
MAINTAINER Thorben Stangenberg <thorben@stangenberg.ch>  
  
# install scala  
RUN FILE=`mktemp`; wget https://dl.bintray.com/sbt/debian/sbt-0.13.6.deb -qO
$FILE && dpkg -i $FILE && rm $FILE  
RUN FILE=`mktemp`; wget
http://downloads.typesafe.com/scala/2.11.2/scala-2.11.2.deb -qO $FILE && dpkg
-i $FILE && rm $FILE  
  
# update and install unzip  
RUN apt-get update  
RUN apt-get install -y unzip  
  
# install typesafe activator  
RUN FILE=`mktemp`; wget http://downloads.typesafe.com/typesafe-
activator/1.2.10/typesafe-activator-1.2.10-minimal.zip -qO $FILE && unzip
$FILE -d /opt/activator && rm $FILE  
RUN ln -s /opt/activator/activator-1.2.10-minimal/activator /bin/activator  
  
# cache some libraries  
RUN cd /tmp && activator new sample play-scala  
RUN cd /tmp/sample && activator dist  
  
# install tutum.co client  
RUN pip install tutum --pre  
  
# housekeeping  
RUN cd /  
RUN rm -rf /tmp/sample  
  
CMD ["/bin/bash"]  

