FROM phusion/baseimage:latest  
  
CMD ["/sbin/my_init"]  
  
LABEL version="1.0"  
  
RUN add-apt-repository ppa:openjdk-r/ppa \  
&& apt-get update \  
&& apt-get install -y openjdk-7-jre unzip \  
&& cd /tmp \  
&& curl -s -O
http://download.oracle.com/glassfish/3.1.2.2/release/glassfish-3.1.2.2.zip \  
&& unzip -q glassfish-3.1.2.2.zip -d /opt \  
&& ln -s /opt/glassfish3 /opt/glassfish  
  
# Administration Server Port  
EXPOSE 4848  
# HTTP Port  
EXPOSE 8080  
# HTTPS Port  
EXPOSE 8181  
# Pure JMX Clients Port  
EXPOSE 8686  
# Message Queue Port  
EXPOSE 7676  
# IIOP Port  
EXPOSE 3700  
# IIOP/SSL Port  
EXPOSE 3820  
# IIOP/SSL Port with Mutual Authentication  
EXPOSE 3920  
RUN cd /opt/glassfish/bin \  
&& ./asadmin create-service  
  
RUN apt-get clean && rm -rf /var/lib/lists/* /tmp/* /var/tmp/*  
  
#ENTRYPOINT ["/etc/init.d/GlassFish_domain1", "start"]  
#ENTRYPOINT /etc/init.d/GlassFish_domain1 start  

