FROM java:openjdk-8-jdk  
  
MAINTAINER Francois Achache <francois.achache@gmail.com>  
  
# Set the PAYARA env variable  
ENV PAYARA_VERSION 4.1.1.162  
ENV PAYARA_HOME /usr/local/payara41  
ENV PATH $PATH:$PAYARA_HOME/bin  
  
# Install payara  
RUN apt-get update && apt-get install -y curl unzip zip inotify-tools && rm
-rf /var/lib/apt/lists/* \  
&& curl -L -o /tmp/payara-$PAYARA_VERSION.zip https://s3-eu-
west-1.amazonaws.com/payara.co/Payara+Downloads/Payara+$PAYARA_VERSION/payara-$PAYARA_VERSION.zip
\  
&& unzip /tmp/payara-$PAYARA_VERSION.zip -d /usr/local \  
&& rm -f /tmp/payara-$PAYARA_VERSION.zip  
  
# Define demo user  
RUN $PAYARA_HOME/bin/asadmin start-domain domain1 \  
&& echo "AS_ADMIN_USERPASSWORD=demo" > pwd.txt \  
&& $PAYARA_HOME/bin/asadmin create-file-user --passwordfile=pwd.txt --groups
USERGP demo \  
&& $PAYARA_HOME/bin/asadmin stop-domain domain1 \  
&& rm pwd.txt  
  
# Expose the ports we're interested in  
EXPOSE 8080 4848 8181  
COPY deploy.sh $PAYARA_HOME/deploy.sh  
  
RUN chmod ug+x $PAYARA_HOME/deploy.sh  
  
WORKDIR $PAYARA_HOME  
  
# verbose mode for foreground mode  
CMD asadmin start-domain --verbose domain1  
  

