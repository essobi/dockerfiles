# Openhab 1.8.3  
# * configuration is injected  
#  
FROM tdeckers/openhab  
MAINTAINER muesliman  
  
ADD http://search.maven.org/remotecontent?filepath=org/python/jython-
installer/2.7.0/jython-installer-2.7.0.jar /tmp/jython-installer-2.7.0.jar  
RUN java -jar /tmp/jython-installer-2.7.0.jar -d /opt/jython-2.7 -s -t all  
ENV PATH /opt/jython-2.7/bin:$PATH  
# bootstrap jython JAR cache  
RUN jython  
RUN rm -rf /tmp/jython-installer-2.7.0.jar  
  
RUN mkdir -p /opt/openhab/lib \  
&& ln -s /opt/jython-2.7/jython.jar /opt/openhab/lib/jython.jar  
  
COPY files/openhab.sh /usr/local/bin/openhab.sh  
  
RUN apt-get -y update \  
&& apt-get -y install openssh-client sshpass \  
&& /bin/echo -e 'Host *\nUseRoaming no' >> /etc/ssh/ssh_config \  
&& apt-get clean  
  
# try to make it SIP  
#RUN apt-get -y update \  
# && apt-get -y install libopal-dev libpt-dev alsa-base unzip build-essential
\  
# && apt-get clean  
#ADD https://github.com/tmakkonen/sipcmd/archive/master.zip /tmp/sipcmd.zip  
#RUN unzip -d /tmp /tmp/sipcmd.zip  
#WORKDIR "/tmp/sipcmd-master/"  
#RUN cd /tmp/sipcmd-master \  
# && make  
#WORKDIR "/"  
#RUN cp /tmp/sipcmd-master/sipcmd /usr/bin/ \  
# && cd ~ \  
# && rm -rf /tmp/sipcmd-master \  
# && rm -f /tmp/sipcmd.zip  
CMD ["/usr/local/bin/boot.sh"]  

