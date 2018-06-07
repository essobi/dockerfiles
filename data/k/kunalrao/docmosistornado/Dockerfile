FROM centos:7  
RUN yum update -y  
  
#Install Libreoffice headless. Default location = /usr/lib64/libreoffice  
#RUN yum install -y libreoffice-headless libreoffice-writer libreoffice-calc
libreoffice- libreoffice-impress libreoffice-langpack-zh-Hans libreoffice-
langpack-zh-Hant libreoffice-langpack-ja ImageMagick curl wget unzip  
#install common tools  
RUN yum install -y wget unzip which  
  
#install libreoffice 5.0.6.3 (/opt/libreoffice5.0)  
RUN wget -q
https://downloadarchive.documentfoundation.org/libreoffice/old/5.0.6.3/rpm/x86_64/LibreOffice_5.0.6.3_Linux_x86-64_rpm.tar.gz
\  
&& mkdir /tmp/LibreOffice \  
&& tar -xzf LibreOffice_5.0.6.3_Linux_x86-64_rpm.tar.gz -C /tmp/LibreOffice \  
&& yum localinstall -y
/tmp/LibreOffice/LibreOffice_5.0.6.3_Linux_x86-64_rpm/RPMS/* \  
&& rm -rf /tmp/LibreOffice  
  
#install openjdk 8  
RUN yum install -y java-1.8.0-openjdk  
  
#Download Docmosis and install  
#Docmosis Install location = /docmosis-tornado  
#Docmosis template store = /docmosis-tornado/template-store  
#Docmosis working directory = /docmosis-tornado/workspace  
RUN mkdir /docmosis-tornado && \  
wget -q
https://www.docmosis.com/download/tornado2.4/docmosisTornado2.4_6366.zip && \  
unzip docmosisTornado2.4_6366.zip -d /docmosis-tornado && \  
rm -f docmosisTornado2.4_6366.zip && \  
mkdir /docmosis-tornado/template-store && \  
mkdir /docmosis-tornado/workspace  
  
#Download a sample template to template store  
RUN yum install -y git && \  
git clone https://kunalrao@bitbucket.org/kunalrao/docmosis-sample-
templates.git && \  
mv docmosis-sample-templates /docmosis-tornado/template-store/  
  
# Set environment variables.  
ENV HOME /docmosis-tornado  
  
# Define working directory.  
WORKDIR /docmosis-tornado  
  
# Define default command.  
CMD ["java","-Dport=8090","-jar","/docmosis-tornado/docmosisTornado2.4.war"]  
#CMD ["java","-version"]

