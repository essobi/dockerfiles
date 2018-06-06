FROM knowagelabs/knowage-server-docker:6.1.1  
  
ENV TZ=Australia/Melbourne \  
STORE_PASS=changme \  
KEY_PASS=changme  
  
COPY ./entrypoint.sh ./  
COPY ./*.sql /home/knowage/mysql/  
  
WORKDIR ${KNOWAGE_DIRECTORY}/${APACHE_TOMCAT_PACKAGE}/bin  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y tzdata && \  
useradd -d ${KNOWAGE_DIRECTORY} -s /bin/false knowage && \  
# install gosu  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" && \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$dpkgArch" && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true && \  
# complete gosu  
rm -rf ${KNOWAGE_DIRECTORY}/${APACHE_TOMCAT_PACKAGE}/webapps/ROOT/* && \  
echo '<% response.sendRedirect("/knowage"); %>' >
${KNOWAGE_DIRECTORY}/${APACHE_TOMCAT_PACKAGE}/webapps/ROOT/index.jsp && \  
rm -rf
${KNOWAGE_DIRECTORY}/${APACHE_TOMCAT_PACKAGE}/webapps/{docs,examples,host-
manager,manager} && \  
chown -R knowage:knowage ${KNOWAGE_DIRECTORY} && \  
chown -R knowage:knowage ${MYSQL_SCRIPT_DIRECTORY}/*.sql && \  
chmod u+x *.sh && \  
# knowage patched jars  
cd /tmp && \  
wget https://github.com/coolersport/knowage-
addon/releases/download/0.3/knowage-core-6.1.1.jar && \  
wget https://github.com/coolersport/knowage-
addon/releases/download/0.3/knowage-utils-6.1.1.jar && \  
for jar in `ls *.jar`; do \  
find ${KNOWAGE_DIRECTORY}/${APACHE_TOMCAT_PACKAGE}/webapps -name $jar -exec cp
$jar {} ';'; \  
done && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["gosu", "knowage", "./startup.sh"]  

