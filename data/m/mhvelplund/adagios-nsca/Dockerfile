# Adagios server  
FROM pschmitt/adagios  
MAINTAINER Mads Hvelplund "mhv@tmnet.dk"  
# Enable git repository  
ENV GIT_REPO true  
  
# Download  
RUN yum -y install tar make automake gcc-c++ syslog  
COPY nsca-2.9.1.tar.gz /download/nsca-2.9.1.tar.gz  
WORKDIR /download  
RUN tar xvzf nsca-2.9.1.tar.gz  
  
# Compile  
WORKDIR /download/nsca-2.9.1  
RUN ./configure  
RUN make all  
RUN cp -v "/download/nsca-2.9.1/src/nsca" "/usr/sbin/nsca"  
WORKDIR /  
  
# Debug  
#ADD test.message /test/test.message  
#RUN cp -v "/download/nsca-2.9.1/src/send_nsca" "/test/send_nsca"  
#RUN cp -v "/download/nsca-2.9.1/sample-config/send_nsca.cfg"
"/test/send_nsca.cfg"  
# Configure  
ADD etc /etc/nagios  
RUN sed -e 's/nagiosadmin/admin/' /etc/nagios/cgi.cfg > /tmp.cfg  
RUN mv -f /tmp.cfg /etc/nagios/cgi.cfg  
RUN chown -R nagios.nagios /etc/nagios  
WORKDIR /etc/nagios  
RUN mv -f _git .git  
RUN mv -f _gitignore .gitignore  
  
ADD supervisord.conf /etc/supervisord.conf  
  
#Cleanup  
RUN rm -rf download  
  
EXPOSE 80 5667

