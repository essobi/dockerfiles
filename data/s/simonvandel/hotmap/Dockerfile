FROM dsferruzza/openjdk  
MAINTAINER Simon Vandel Sillesen <simon.vandel@gmail.com>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Show versions  
RUN java -version  
RUN javac -version  
  
# Select Activator version  
ENV ACTIVATOR_VERSION 1.3.9  
ENV SBT_VERSION 0.13.11  
# Install tools  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
unzip \  
sshpass \  
npm \  
curl \  
git  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs  
RUN npm install -g npm  
RUN npm install -g webpack  
  
# Get Activator  
RUN cd /tmp && \  
wget --progress=dot:mega https://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \  
unzip typesafe-activator-$ACTIVATOR_VERSION.zip && \  
mkdir /opt/typesafe && \  
mv /tmp/activator-dist-$ACTIVATOR_VERSION /opt/typesafe/activator-
dist-$ACTIVATOR_VERSION && \  
ln -s /opt/typesafe/activator-dist-$ACTIVATOR_VERSION/bin/activator
/usr/local/bin/activator && \  
rm /tmp/typesafe-activator-$ACTIVATOR_VERSION.zip && \  
# Run Activator to cache its dependencies  
cd /tmp && \  
activator new init play-scala && \  
cd /tmp/init && \  
#sed -i "s/sbt.version=0.13.8/sbt.version=$SBT_VERSION/"
project/build.properties && \  
activator about && \  
rm -fr /tmp/init && \  
# Slim down image  
apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/??
/usr/share/man/??_*  

