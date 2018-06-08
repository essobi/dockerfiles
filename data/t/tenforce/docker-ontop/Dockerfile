FROM tenforce/tomcat  
  
MAINTAINER Bert Van Nuffelen <bert.van.nuffelen@tenforce.com>  
  
# open the port for the mssql jdbc driver  
# this is oslo specific  
EXPOSE 1433  
RUN apt-get install -y zip  
  
ADD contexts /contexts  
ADD myconfig /myconfig  
ADD releases /releases  
  
#RUN wget
https://sourceforge.net/projects/ontop4obda/files/ontop-1.17.0/ontop-sesame-
webapps-1.17.0.zip/download  
#RUN wget
https://sourceforge.net/projects/ontop4obda/files/ontop-1.18.0/ontop-sesame-
webapps-1.18.0.1.zip/download  
#RUN mv download /webapps/ontop.zip  
#RUN unzip /webapps/ontop.zip  
ENTRYPOINT ["/myconfig/run.sh"]  
  

