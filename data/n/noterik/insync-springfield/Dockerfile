#Ubuntu with Java, Tomcat, ffmpeg, ffprobe  
FROM ubuntu:16.04  
ARG git_api_token=null  
ENV GITHUB_ACCESS_TOKEN=$git_api_token  
  
ENV TOMCAT_VERSION 8.5.23  
#Install dependencies  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y git build-essential curl wget software-properties-common
libtiff5 libtiff5-dev imagemagick  
  
#Create Springfield directory  
RUN mkdir -p /springfield  
  
#Install JDK 8  
RUN apt-get install -y openjdk-8-jre  
  
#Install Tomcat  
RUN wget --quiet --no-cookies
https://archive.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \  
tar xzvf /tmp/tomcat.tgz -C /springfield && \  
mv /springfield/apache-tomcat-${TOMCAT_VERSION} /springfield/tomcat && \  
rm /tmp/tomcat.tgz && \  
rm -rf /springfield/tomcat/webapps/examples && \  
rm -rf /springfield/tomcat/webapps/docs  
  
#Add entry point  
COPY ./docker-entrypoint.sh /springfield/docker-entrypoint.sh  
  
RUN chmod +x /springfield/docker-entrypoint.sh  
  
#Add admin/admin user  
COPY tomcat/tomcat-users.xml /springfield/tomcat/conf/  
COPY tomcat/context.xml /springfield/tomcat/webapps/manager/META-INF/  
COPY tomcat/password.conf /springfield/tomcat/conf/  
  
ENV CATALINA_HOME /springfield/tomcat  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
#Install ffmpeg  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:jonathonf/ffmpeg-3 -y && \  
apt-get update && \  
apt-get install -y ffmpeg libav-tools x264 x265  
  
#Add homer/config.template.xml  
RUN mkdir -p /springfield/homer  
COPY homer/config.template.xml /springfield/homer/  
  
#Install fetch for easy retrieval of private repos  
RUN curl -L https://github.com/gruntwork-
io/fetch/releases/download/v0.1.1/fetch_linux_amd64 -o /usr/bin/fetch  
RUN chmod +x /usr/bin/fetch  
  
#Add smithers  
RUN mkdir -p /springfield/smithers/jars  
RUN fetch --repo="https://github.com/Noterik/marin-addons" \--github-oauth-
token="${GITHUB_ACCESS_TOKEN}" \--branch="standalone-adjustment" \--source-
path="build/marin-addons.jar" /springfield/smithers/jars/marin-addons.jar  
RUN curl -L https://github.com/Noterik/smithers/raw/master/dist/smithers2.war
-o /springfield/tomcat/webapps/smithers2.war  
  
#Add momar transcoding profiles  
RUN mkdir -p /springfield/momar/batchfiles  
RUN git clone https://${GITHUB_ACCESS_TOKEN}:@github.com/Noterik/mediamix-
transcoding-profiles.git /springfield/momar/batchfiles/  
RUN curl -L https://github.com/Noterik/momar/raw/master/war/momar.war -o
/springfield/tomcat/webapps/momar.war  
  
#Add nelson  
RUN mkdir -p /springfield/nelson/temp  
RUN fetch --repo="https://github.com/Noterik/nelson" \--github-oauth-
token="${GITHUB_ACCESS_TOKEN}" \--branch="master" \--source-
path="war/nelson.war" /springfield/tomcat/webapps/nelson.war  
  
#Add flanders  
RUN mkdir -p /springfield/flanders/temp  
RUN curl -L https://github.com/Noterik/flanders/raw/master/war/flanders.war -o
/springfield/tomcat/webapps/flanders.war  
  
#Add bart  
RUN curl -L https://github.com/Noterik/bart/raw/master/dist/bart.war -o
/springfield/tomcat/webapps/bart.war  
  
#Add stageplayer-hdf5-reader  
RUN fetch --repo="https://github.com/Noterik/stageplayer-hdf5-reader"
\--github-oauth-token="${GITHUB_ACCESS_TOKEN}" \--branch="master" \--source-
path="war/stageplayer-hdf5-reader.war"
/springfield/tomcat/webapps/stageplayer-hdf5-reader.war  
  
#Add mojo to tomcat libs  
RUN curl -L https://github.com/Noterik/mojo/raw/master/build/mojo.jar -o
/springfield/tomcat/lib/mojo.jar  
  
#Add all other tomcat libs  
RUN wget --quiet --no-cookies http://insync.noterik.com/insync-
installation/tomcat-libs.tar.gz -O /tmp/tomcat-libs.tar.gz && \  
tar xvf /tmp/tomcat-libs.tar.gz -C /springfield/tomcat/lib && \  
rm /tmp/tomcat-libs.tar.gz  
  
#Add IDT SDK  
#RUN wget --quiet --no-cookies
https://media.idtvision.com/software/sdk/xstream_2.12.21_amd64.deb -O
/tmp/xstream_2.12.21_amd64.deb && \  
# dpkg -i /tmp/xstream_2.12.21_amd64.deb && \  
# rm /tmp/xstream_2.12.21_amd64.deb  
RUN wget --quiet --no-cookies https://insync.noterik.com/insync-
installation/xstream_2.12.15_amd64.deb -O /tmp/xstream_2.12.15_amd64.deb && \  
dpkg -i /tmp/xstream_2.12.15_amd64.deb && \  
rm /tmp/xstream_2.12.15_amd64.deb  
  
#Add idt_raw  
RUN mkdir -p /tmp/idt_raw && \  
git clone https://${GITHUB_ACCESS_TOKEN}:@github.com/Noterik/idt_raw.git
/tmp/idt_raw/ && \  
cd /tmp/idt_raw && \  
make && \  
mv /tmp/idt_raw/idt_raw /usr/bin/ && \  
rm -rf /tmp/idt_raw  
  
#Add HDF support  
RUN curl -L https://support.hdfgroup.org/ftp/HDF5/releases/HDF-
JAVA/hdfjni-3.3.2/bin/HDFJava-3.3.2_Stat-centos7_64.tar.gz -o
/springfield/HDFJava-3.3.2_Stat-centos7_64.tar.gz && \  
tar -xvf /springfield/HDFJava-3.3.2_Stat-centos7_64.tar.gz -C /springfield &&
\  
chmod 777 /springfield/hdf/HDFJava-3.3.2-Linux.sh && \  
/springfield/hdf/HDFJava-3.3.2-Linux.sh --include-subdir --skip-license
--prefix=/springfield/hdf -y  
ENV JAVA_OPTS="$JAVA_OPTS \  
-Djavax.xml.parsers.DocumentBuilderFactory=com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderFactoryImpl \  
-Djava.library.path=/springfield/hdf/HDFJava-3.3.2-Linux/HDF_Group/HDFJava/3.3.2/lib "  
#Add InSync dir  
RUN mkdir -p /export/insync  
  
#Clean  
RUN apt-get clean  
  
EXPOSE 8080  
#Launch Tomcat  
ENTRYPOINT ["/springfield/docker-entrypoint.sh"]  

