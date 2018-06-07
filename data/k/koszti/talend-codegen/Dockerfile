FROM openjdk:latest  
LABEL maintainer peter.kosztolanyi@gmail.com  
  
ENV
TALEND_DOWNLOAD_URL=https://sourceforge.net/projects/talendesb/files/Talend%20Open%20Studio%20for%20ESB/5.6.2/TOS_ESB-20150508_1414-V5.6.2.zip/download  
ENV TALEND_CODEGEN_GIT_REPO=https://github.com/kakwa/talend-codegen.git  
ENV TALEND_DIR=/opt/talend  
ENV TALEND_CODEGEN_DIR=/opt/talend-codegen  
  
# Update ubuntu  
RUN apt-get update && apt-get install -y make ant  
  
# Download Talend ESB  
RUN wget --no-check-certificate -O $TALEND_DIR.zip $TALEND_DOWNLOAD_URL &&
unzip $TALEND_DIR.zip -d /opt  
  
# Compile Command Line Code Generation (job-export) Talend plugin  
RUN git clone $TALEND_CODEGEN_GIT_REPO $TALEND_CODEGEN_DIR && cd
$TALEND_CODEGEN_DIR && make  

