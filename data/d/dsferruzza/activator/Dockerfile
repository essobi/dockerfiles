FROM dsferruzza/openjdk  
MAINTAINER David Sferruzza <david.sferruzza@gmail.com>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Show versions  
RUN java -version  
RUN javac -version  
  
# Select Activator version  
ENV ACTIVATOR_VERSION 1.3.12  
ENV SBT_VERSION 0.13.13  
ENV SCALA_VERSION 2.12.1  
ENV COURSIER_VERSION 1.0.0-M15-1  
# Install tools  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
unzip  
  
# Get Activator  
ENV ACTIVATOR_NAME=activator-$ACTIVATOR_VERSION-minimal  
RUN cd /tmp && \  
wget --progress=dot:mega https://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-$ACTIVATOR_NAME.zip && \  
unzip typesafe-$ACTIVATOR_NAME.zip && \  
mkdir /opt/typesafe && \  
mv /tmp/$ACTIVATOR_NAME /opt/typesafe/$ACTIVATOR_NAME && \  
ln -s /opt/typesafe/$ACTIVATOR_NAME/bin/activator /usr/local/bin/activator &&
\  
rm /tmp/typesafe-$ACTIVATOR_NAME.zip && \  
# Use coursier  
mkdir -p ~/.sbt/0.13/plugins && \  
echo "addSbtPlugin(\"io.get-coursier\" % \"sbt-coursier\" %
\"$COURSIER_VERSION\")" >> ~/.sbt/0.13/plugins/build.sbt && \  
# Run Activator to cache its dependencies  
cd /tmp && \  
activator new init minimal-scala && \  
cd /tmp/init && \  
sed -i "s/sbt.version=0.13.8/sbt.version=$SBT_VERSION/"
project/build.properties && \  
sed -i "s/2.11.7/$SCALA_VERSION/" build.sbt && \  
cat build.sbt && cat project/build.properties && \  
activator about && \  
rm -fr /tmp/init && \  
# Slim down image  
apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/??
/usr/share/man/??_*  

