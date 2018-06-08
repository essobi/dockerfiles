FROM pierrecarre/java-centos:oracle-5-jdk  
MAINTAINER Pierre CARRE <pierre.carre78@gmail.com>  
  
RUN yum -y install tar \  
&& yum -y clean all  
  
RUN cd /opt \  
&& curl -L 'http://archive.apache.org/dist/ant/binaries/apache-
ant-1.6.5-bin.tar.gz' \  
-o apache-ant-1.6.5-bin.tar.gz \  
&& tar xzf apache-ant-1.6.5-bin.tar.gz \  
&& rm -rf apache-ant-1.6.5-bin.tar.gz  
  
RUN cd /opt \  
&& curl -L
'http://archive.apache.org/dist/jakarta/bcel/old/v5.1/bcel-5.1.tar.gz' \  
-o bcel-5.1.tar.gz \  
&& tar xzf bcel-5.1.tar.gz \  
&& cp /opt/bcel-5.1/bcel-5.1.jar /opt/apache-ant-1.6.5/lib/bcel-5.1.jar \  
&& rm -rf bcel-5.1*  
  
RUN cd /opt \  
&& curl -L
'http://download.fr.forge.objectweb.org/jonas/jonas4.10.9-tomcat5.5.28.tgz' \  
-o jonas4.10.9-tomcat5.5.28.tgz \  
&& tar xzf jonas4.10.9-tomcat5.5.28.tgz \  
&& rm -rf jonas4.10.9-tomcat5.5.28.tgz  
  
# Set environment variables.  
ENV HOME /root  
ENV ANT_HOME /opt/apache-ant-1.6.5  
ENV JONAS_ROOT /opt/JONAS_4_10_9  
ENV JONAS_BASE /opt/jonas_base  
ENV PATH $JONAS_ROOT/bin/unix:$ANT_HOME/bin:$PATH  
  
# Create JOnAS base.  
RUN cd $JONAS_ROOT && ant create_jonasbase  
  
# Define working directory.  
WORKDIR /root  
  
# Expose port.  
EXPOSE 9000  
# Define default command.  
#CMD ["bash"]  
CMD ["/opt/JONAS_4_10_9/bin/unix/jonas", "-fg", "start"]  

