#######################################################################  
# Create an extensible SoapUI mock service runner image using CentOS  
#######################################################################  
  
FROM openjdk:8-jre-alpine  
  
MAINTAINER prop <propoff@gmail.com>  
  
# Update the system  
  
RUN apk update  
  
##########################################################  
# Download and unpack soapui  
##########################################################  
  
RUN apk add shadow && apk add wget && \  
groupadd -r soapui && useradd -r -g soapui -m -d /home/soapui soapui  
  
RUN wget --no-check-certificate --no-cookies --quiet
http://cdn01.downloads.smartbear.com/soapui/5.2.1/SoapUI-5.2.1-linux-
bin.tar.gz && \  
echo "ba51c369cee1014319146474334fb4e1 SoapUI-5.2.1-linux-bin.tar.gz" >>
MD5SUM && \  
md5sum -c MD5SUM && \  
tar -xzf SoapUI-5.2.1-linux-bin.tar.gz -C /home/soapui && \  
rm -f SoapUI-5.2.1-linux-bin.tar.gz MD5SUM  
  
RUN chown -R soapui:soapui /home/soapui  
RUN find /home/soapui -type d -exec chmod 770 {} \;  
RUN find /home/soapui -type f -exec chmod 660 {} \;  
  
RUN wget --no-check-certificate --no-cookies --quiet -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.3/gosu-amd64" && \  
chmod +x /usr/local/bin/gosu  
  
############################################  
# Setup MockService runner  
############################################  
  
USER soapui  
ENV HOME /home/soapui  
ENV SOAPUI_DIR /home/soapui/SoapUI-5.2.1  
ENV SOAPUI_PRJ /home/soapui/soapui-prj  
  
############################################  
# Add customization sub-directories (for entrypoint)  
############################################  
ADD docker-entrypoint-initdb.d /docker-entrypoint-initdb.d  
ADD soapui-prj $SOAPUI_PRJ  
  
############################################  
# Expose ports and start SoapUI mock service  
############################################  
USER root  
  
EXPOSE 8080  
  
COPY docker-entrypoint.sh /  
RUN chmod 700 /docker-entrypoint.sh  
RUN chmod 770 $SOAPUI_DIR/bin/*.sh  
  
RUN chown -R soapui:soapui $SOAPUI_PRJ  
RUN find $SOAPUI_PRJ -type d -exec chmod 770 {} \;  
RUN find $SOAPUI_PRJ -type f -exec chmod 660 {} \;  
  
RUN apk del wget shadow  
  
############################################  
# Start SoapUI mock service runner  
############################################  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["start-soapui"]  

