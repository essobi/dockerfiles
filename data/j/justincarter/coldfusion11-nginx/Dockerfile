FROM buildpack-deps:jessie-curl  
  
# add coldfusion 11 silent install configs  
COPY /coldfusion/installer.profile /tmp/  
COPY /coldfusion/hotfix.properties /tmp/  
  
# download and install coldfusion 11  
RUN curl -L http://daemon-provisioning-
resources.s3.amazonaws.com/coldfusion/ColdFusion_11_WWEJ_linux64.bin -o
/tmp/ColdFusion_11_WWEJ_linux64.bin && \  
curl -L https://cfdownload.adobe.com/pub/adobe/coldfusion/11/hotfix_011.jar -o
/tmp/hotfix_011.jar && \  
chmod +x /tmp/ColdFusion_11_WWEJ_linux64.bin && \  
/tmp/ColdFusion_11_WWEJ_linux64.bin -f /tmp/installer.profile && \  
/opt/coldfusion11/cfusion/bin/coldfusion start && \  
sleep 120 && \  
wget --delete-after
http://127.0.0.1:8500/CFIDE/administrator/index.cfm?configServer=true && \  
/opt/coldfusion11/cfusion/bin/coldfusion stop && \  
/opt/coldfusion11/jre/bin/java -jar /tmp/hotfix_011.jar -i silent -f
/tmp/hotfix.properties && \  
rm -rf /tmp/*  
  
# install nginx and supervisord  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
nginx \  
supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add coldfusion 11 start script  
COPY /coldfusion/run.sh /opt/coldfusion11/cfusion/bin/  
RUN chmod -R +x /opt/coldfusion11/cfusion/bin/run.sh  
  
# copy configs  
COPY /coldfusion/adminconfig.xml /opt/coldfusion11/cfusion/lib/  
COPY /nginx/nginx.conf /etc/nginx/  
COPY /nginx/default.conf /etc/nginx/conf.d/  
COPY /supervisor/supervisord.conf /etc/supervisor/conf.d/  
  
EXPOSE 80 8500  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

