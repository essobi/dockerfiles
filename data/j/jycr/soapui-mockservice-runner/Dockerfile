#######################################################################  
# Create an extensible SoapUI mock service runner image using CentOS  
#######################################################################  
  
FROM openjdk:8-jre-alpine  
  
ARG user=soapui  
ARG group=soapui  
ARG uid=1000  
ARG gid=1000  
ARG http_port=8080  
  
ENV HOME /home/soapui  
ENV SOAPUI_DIR /opt/soapui  
ENV SOAPUI_PRJ $HOME/soapui-prj  
ENV SOAPUI_USER ${user}  
  
ENV SOAPUI_SHA512
7b1fa050e5686d7b787e286f6fe29a54526244948cfac5ca8d547b1918b471c4e8eb124f86f1742c775928f4456d0e07bee4a0d95668c74e82a79dbddc3fa934  
ENV SOAPUI_VERSION 5.4.0  
ENV SOAPUI_DOWNLOAD_URL
https://s3.amazonaws.com/downloads.eviware/soapuios/${SOAPUI_VERSION}/SoapUI-${SOAPUI_VERSION}-linux-
bin.tar.gz  
  
COPY docker-entrypoint.sh /  
  
##########################################################  
# Download and unpack soapui  
##########################################################  
  
RUN set -ex; \  
apk add --no-cache --virtual .run-deps \  
su-exec  
  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps \  
shadow \  
curl \  
tar \  
&& groupadd -g ${gid} ${group} \  
&& useradd -r -g ${group} -m -d ${HOME} ${user} \  
&& curl -fSL -o soapui.tgz "${SOAPUI_DOWNLOAD_URL}" \  
&& echo "${SOAPUI_SHA512} *soapui.tgz" | sha512sum -c - \  
&& mkdir -p $SOAPUI_PRJ \  
&& mkdir -p $SOAPUI_DIR \  
&& tar --extract --file soapui.tgz --strip-components 1 \--directory
$SOAPUI_DIR \  
&& rm -f soapui.tgz \  
&& rm -rf $SOAPUI_DIR/Tutorials $SOAPUI_DIR/wsi-test-tools \  
&& chmod 555 /docker-entrypoint.sh \  
&& chmod 555 $SOAPUI_DIR/bin/*.sh \  
&& chown -R ${user}:${group} $HOME \  
&& find $SOAPUI_PRJ -type d -exec chmod 770 {} \; \  
&& find $SOAPUI_PRJ -type f -exec chmod 660 {} \; \  
&& apk del .fetch-deps  
  
  
############################################  
# Setup MockService runner  
############################################  
  
############################################  
# Add customization sub-directories (for entrypoint)  
############################################  
ADD docker-entrypoint-initdb.d /docker-entrypoint-initdb.d  
ADD soapui-prj $SOAPUI_PRJ  
  
############################################  
# Expose ports and start SoapUI mock service  
############################################  
  
EXPOSE ${http_port}  
  
  
############################################  
# Start SoapUI mock service runner  
############################################  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["start-soapui"]  

