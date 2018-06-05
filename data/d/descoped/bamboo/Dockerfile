FROM descoped/atlassian-base  
MAINTAINER Ove Ranheim <oranheim@gmail.com>  
  
# Install Bamboo  
ENV BAMBOO_VERSION 5.15.0.1  
ENV BAMBOO_INST /opt/bamboo  
ENV BAMBOO_HOME /var/atlassian-home  
  
ENV UID bamboo  
ENV GID atlassian  
  
ADD configure.bash /configure  
RUN chmod +x /configure  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y ssh-client git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -Lk
http://www.atlassian.com/software/bamboo/downloads/binary/atlassian-
bamboo-$BAMBOO_VERSION.tar.gz -o /root/bamboo.tar.gz \  
&& useradd -r --create-home --home-dir $BAMBOO_INST \--groups $GID \--shell
/bin/bash $UID \  
&& tar zxf /root/bamboo.tar.gz --strip=1 -C $BAMBOO_INST \  
&& rm /root/bamboo.tar.gz \  
&& echo "bamboo.home=$BAMBOO_HOME" > $BAMBOO_INST/atlassian-bamboo/WEB-
INF/classes/bamboo-init.properties \  
&& mv $BAMBOO_INST/conf/server.xml $BAMBOO_INST/conf/server-backup.xml  
  
# Launching Bamboo  
WORKDIR $BAMBOO_INST  
VOLUME ["$BAMBOO_HOME"]  
  
COPY entrypoint.bash /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 8085 54663  
CMD ["bin/start-bamboo.sh", "-fg"]  

