FROM node:8.4.0  
  
ENV S3_TMP /tmp/s3cmd.zip  
ENV S3_ZIP /tmp/s3cmd-master  
ENV RDS_TMP /tmp/RDSCLi.zip  
ENV RDS_VERSION 1.19.004  
ENV JAVA_HOME /usr/lib/jvm/default-jvm  
ENV AWS_RDS_HOME /usr/local/RDSCli-${RDS_VERSION}  
ENV PATH ${PATH}:${AWS_RDS_HOME}/bin:${JAVA_HOME}/bin:${AWS_RDS_HOME}/bin  
ENV PAGER more  
  
WORKDIR /tmp  
  
#============================================  
# Google Chrome  
#============================================  
ARG CHROME_VERSION="google-chrome-stable"  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install \  
${CHROME_VERSION:-google-chrome-stable} \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
#============================================  
# Other dependencies  
#============================================  
RUN apt-get update && apt-get install -y \  
python \  
python-pip \  
python-dev \  
netcat \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install awscli  

