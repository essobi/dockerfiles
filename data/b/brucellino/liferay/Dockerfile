#  
# Installs Liferay 6.1.1 bundles and changes glassfish administrative
password.  
#  
FROM brucellino/jdk7  
  
MAINTAINER Mario Torrisi <mario.torrisi@ct.infn.it>  
  
RUN apt-get update && apt-get install -y wget unzip pwgen expect  
  
# Download and unzip liferay 6.1.1 glassfish bundle  
RUN wget
"https://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.1.1%20GA2/liferay-
portal-glassfish-6.1.1-ce-ga2-20120731132656558.zip" && \  
unzip liferay-portal-glassfish-6.1.1-ce-ga2-20120731132656558.zip -d /opt && \  
rm liferay-portal-glassfish-6.1.1-ce-ga2-20120731132656558.zip && \  
apt-get clean  
  
# Sets exec permissions to asadmin file  
RUN chmod +x /opt/liferay-portal-6.1.1-ce-ga2/glassfish-3.1.2/bin/asadmin  
  
# Sets env var to glassfish bin  
ENV PATH /opt/liferay-portal-6.1.1-ce-ga2/glassfish-3.1.2/bin:$PATH  
  
ADD run.sh /run.sh  
ADD change_admin_password.sh /change_admin_password.sh  
ADD change_admin_password_func.sh /change_admin_password_func.sh  
ADD enable_secure_admin.sh /enable_secure_admin.sh  
RUN chmod +x /*.sh  
  
# 4848 (administration), 8080 (HTTP listener), 8181 (HTTPS listener)  
EXPOSE 4848 8080 8181  
CMD ["/run.sh"]  

