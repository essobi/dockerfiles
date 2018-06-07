FROM greatfox/tomcat8  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
RUN mkdir -p /var/jspwiki/page \  
/var/jspwiki/attachment \  
/var/jspwiki/log \  
/var/jspwiki/work  
RUN chown -R tomcat8:tomcat8 /var/jspwiki  
  
RUN wget -O /tmp/jspwiki-wikipages-zh_CN-2.10.1.zip
https://www.apache.org/dist/jspwiki/2.10.1/wikipages/jspwiki-wikipages-
zh_CN-2.10.1.zip  
RUN apt-get -y install unzip  
RUN unzip -d /tmp/ /tmp/jspwiki-wikipages-zh_CN-2.10.1.zip  
RUN mv /tmp/jspwiki-wikipages-zh_CN-2.10.1/* /var/jspwiki/page/  
  
RUN rm -Rf /tmp/jspwiki*  
RUN rm -Rf /opt/tomcat8/webapps/*  
RUN wget -O /opt/tomcat8/webapps/ROOT.war
https://www.apache.org/dist/jspwiki/2.10.1/binaries/JSPWiki.war  
  
RUN echo 'jspwiki.baseURL = http:/// \n\  
jspwiki.applicationName = Wiki \n\  
jspwiki.referenceStyle = relative \n\  
jspwiki.pageProvider =VersioningFileProvider \n\  
jspwiki.usePageCache = true \n\  
jspwiki.fileSystemProvider.pageDir = /var/jspwiki/page \n\  
jspwiki.basicAttachmentProvider.storageDir = /var/jspwiki/attachment \n\  
jspwiki.workDir = /var/jspwiki/work \n\  
jspwiki.translatorReader.matchEnglishPlurals = false \n\  
jspwiki.lucene.analyzer =
org.apache.lucene.analysis.standard.cn.ChineseAnalyzer \n\  
jspwiki.urlConstructor = ShortURLConstructor \n\  
jspwiki.defaultprefs.template.language = cn \n\  
log4j.appender.FileLog.File = /var/jspwiki/log/jspwiki.log' >>
/opt/tomcat8/lib/jspwiki-custom.properties  
  

