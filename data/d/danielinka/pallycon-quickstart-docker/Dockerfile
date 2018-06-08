FROM deliveryagent/centos7-node  
MAINTAINER Daniel Kim <daniel@inka.co.kr>  
  
# Install required utils  
RUN yum -y update  
RUN yum -y install unzip  
RUN yum -y install git  
  
# Create node app and packager directory  
# Download app source from github repository  
WORKDIR /usr/src  
RUN git clone https://github.com/inka-pallycon/pallycon-quickstart-node.git
app  
# RUN wget "http://sample.pallycon.com/quickstart/qs_node_app.zip" && unzip
qs_node_app.zip  
# Install app dependencies  
WORKDIR /usr/src/app  
RUN npm install  
  
# Bundle app source and give scripts permission  
# COPY app/. /usr/src/app  
# RUN chmod 744 /usr/src/app/packager/*.sh  
# Download and unzip prepacked sample video from pallycon server  
# RUN mkdir -p /usr/src/app/website/contents  
# WORKDIR /usr/src/app/website/contents  
# RUN wget "http://sample.pallycon.com/quickstart/bbb.zip" && unzip bbb.zip  
# Download CLI packager and Bento4 from pallycon server  
RUN mkdir -p /usr/src/app/packager  
WORKDIR /usr/src/app/packager  
RUN wget
"http://sample.pallycon.com/quickstart/PallyCon_Packager_DASHCENC_CLI_CentOS_20160607.zip"  
RUN unzip PallyCon_Packager_DASHCENC_CLI_CentOS_20160607.zip  
RUN chmod 744 /usr/src/app/packager/PallyConPackager  
  
RUN wget
"http://sample.pallycon.com/quickstart/Bento4-SDK-1-5-0-613.x86_64-unknown-
linux.zip"  
RUN unzip Bento4-SDK-1-5-0-613.x86_64-unknown-linux.zip && mv
Bento4-SDK-1-5-0-613.x86_64-unknown-linux Bento4  
  
# setting directory for host volume  
RUN mkdir -p /usr/src/app/data  
VOLUME ["/usr/src/app/data"]  
  
# RUN mkdir -p /usr/src/app/website/gateway  
# VOLUME ["/usr/local/work", "/usr/src/app/website/gateway"]  
EXPOSE 8080  
WORKDIR /usr/src/app  
CMD ["node", "server.js"]  

