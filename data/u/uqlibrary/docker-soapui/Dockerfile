FROM java:openjdk-8-jre  
  
# env vars  
ENV SOAPUI_VERSION 5.3.0  
ENV PORT 8088  
# download and unarchive soapui  
RUN mkdir -p /data && mkdir -p /opt &&\  
curl
http://cdn01.downloads.smartbear.com/soapui/${SOAPUI_VERSION}/SoapUI-${SOAPUI_VERSION}-linux-
bin.tar.gz \  
| gunzip -c - | tar -xf - -C /opt && \  
ln -s /opt/SoapUI-${SOAPUI_VERSION} /opt/SoapUI  
# set environment  
ENV PATH ${PATH}:/opt/SoapUI/bin  
  
# expose port  
EXPOSE ${PORT}  
  
# set working directory  
WORKDIR /data  
  
# install entrypoint  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
# execute entrypoint  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

