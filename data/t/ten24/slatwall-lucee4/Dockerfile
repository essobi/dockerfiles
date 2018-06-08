# Slatwall Quickstart for running locally for evaluation only  
FROM lucee/lucee4:latest  
MAINTAINER Sumit Verma, sumit.verma@ten24web.com  
  
ENV BRANCH master  
ENV UPDATE false  
ENV LUCEE_PASSWORD slatwall  
  
RUN wget -nv https://github.com/ten24/slatwall/archive/${BRANCH}.zip -O
/root/slatwall.zip && \  
unzip /root/slatwall.zip -d /root/slatwall && \  
cp -a /root/slatwall/slatwall-${BRANCH}/. /var/www && \  
rm -rf /root/slatwall.zip && \  
rm -rf /root/slatwall  
  
# Copy over the Lucee Configs  
COPY lucee-server.xml /opt/lucee/server/lucee-server/context/lucee-server.xml  
COPY lucee-web.xml.cfm /opt/lucee/web/lucee-web.xml.cfm  
  
# Move the configFramework.cfm file to the root so that it can be moved into
Slatwall after install  
COPY configFramework.cfm /root/configFramework.cfm  
  
# Copy over the entrypoint  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Expose Lucee Port  
EXPOSE 8888  
CMD ["catalina.sh","run"]  

