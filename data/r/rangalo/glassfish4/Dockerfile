FROM rangalo/java8  
  
MAINTAINER rangalo "hard.mehta@gmail.com"  
RUN wget -q --no-cookies --no-check
http://download.java.net/glassfish/4.1/release/glassfish-4.1.zip && \  
mv -v glassfish-4.1.zip /opt/oracle/ && \  
cd /opt/oracle && unzip -q glassfish-4.1.zip && \  
ln -svn /opt/oracle/glassfish4 /opt/oracle/glassfish && \  
rm -f /opt/oracle/glassfish-4.1.zip && \  
echo "GLASSFISH_HOME=/opt/oracle/glassfish"  
  
ENV GLASSFISH_HOME /opt/oracle/glassfish  
ENV PATH $GLASSFISH_HOME/bin:$PATH  
  
ADD run.sh /run.sh  
ADD change_admin_pass.expect /change_admin_pass.expect  
ADD enable_secure_login.expect /enable_secure_login.expect  
  
RUN chmod +x run.sh && \  
chmod +x *.expect  
  
# 4848 (administration), 8080 (HTTP listener), 8181 (HTTPS listener)  
EXPOSE 4848 8080 8181  
CMD ["/run.sh"]  

