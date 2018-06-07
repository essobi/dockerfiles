FROM hawkular/docker-maven  
MAINTAINER Matt Mahoney <mmahoney@redhat.com> USER root  
ENV PATH .:$PATH RUN echo "root:redhat" | chpasswd  
RUN yum -y install wget git openssh-server httpd supervisor  
  
RUN groupadd hudson  
RUN useradd -m -g hudson -s /bin/bash hudson  
RUN echo "hudson:hudson" | chpasswd  
  
RUN mkdir /var/run/sshd  
RUN ssh-keygen -A  
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
# Install ant  
WORKDIR /usr/lib  
RUN wget http://archive.apache.org/dist/ant/binaries/apache-
ant-1.9.4-bin.tar.gz  
RUN tar -xvf apache-ant-1.9.4-bin.tar.gz; rm apache-ant-1.9.4-bin.tar.gz  
ENV PATH /usr/lib/apache-ant-1.9.4/bin:$PATH  
ENV ANT_HOME /usr/lib/apache-ant-1.9.4  
RUN mkdir -p /var/www/html/hawkular-test-results/debug; chmod -R 777
/var/www/html/hawkular-test-results/debug  
RUN echo "Hawkular Test Results Directory" > /var/www/html/hawkular-test-
results/Hawkular-README.txt  
  
RUN printf "\n[supervisord]\nnodaemon=true\n\  
[program:sshd]\ncommand=/bin/bash -c /usr/sbin/sshd\n\  
[program:httpd]\ncommand=/bin/bash -c /usr/sbin/httpd\n" >>
/etc/supervisord.conf  
RUN printf "\n[program:hawkuklar-test]\ncommand=/bin/bash -x
/home/hudson/start.sh\n" >> /etc/supervisord.conf  
  
EXPOSE 22 80  
USER hudson  
WORKDIR /home/hudson  
  
ENV PATH .:$PATH  
RUN git clone https://github.com/RedHatQE/hawkular-smoke-test.git  
  
# Install JMeter  
RUN cd /home/hudson; git clone https://github.com/apache/jmeter.git; cd
jmeter; ant download_jars; ant  
  
# Install Hakular Sauce Labs tests  
RUN git clone https://github.com/ahovsepy/hawkular-ui-test.git  
RUN cd hawkular-ui-test; mvn clean install -DskipTests  
RUN printf "1=firefox:24.0:Linux" > /home/hudson/hawkular-ui-
test/src/test/resources/browserAndOs.properties  
  
# Install Hawkular Java Client - Run tests - Runs against localhost:8080  
RUN git clone https://github.com/Hawkular-QE/hawkular-java-client.git  
RUN cd hawkular-java-client; mvn clean install -DskipTests dependency:go-
offline  
  
# Create start script to run tests  
RUN printf "\  
"#!"/bin/bash\n\  
export HAWKULAR_ENDPOINT=\$IP\n\  
echo IP \$IP >> /var/www/html/hawkular-test-results/debug/debug-info.txt\n\  
echo HAWKULAR_ENDPOINT \$HAWKULAR_ENDPOINT >> /var/www/html/hawkular-test-
results/debug/debug-info.txt\n\  
df >> /var/www/html/hawkular-test-results/debug/debug-info.txt\n\  
sleep 2m;\n\  
cd /home/hudson/hawkular-smoke-test/tests;\n\  
testRunner.sh > /var/www/html/hawkular-test-results/script-test-
results.txt;\n\  
wget --retry-connrefused --timeout=10 -t 50 -w 5 --spider \$IP\n\  
cd /home/hudson/hawkular-ui-test; mvn test -DhawkularUrl=\$IP
-DauthenticationKey=\$AUTH_KEY > /var/www/html/hawkular-test-results/debug/ui-
debug.txt 2>&1; cp /home/hudson/hawkular-ui-test/target/surefire-
reports/testng-results.xml /var/www/html/hawkular-test-results/ui-test-
results.xml; cp /home/hudson/hawkular-ui-test/target/surefire-
reports/emailable-report.html /var/www/html/hawkular-test-results/ui-test-
results.html\n\  
"#"cd /home/hudson/hawkular-java-client; mvn -U test -Pci >
/var/www/html/hawkular-test-results/debug/rest-client-debug.txt 2>&1; cp
/home/hudson/hawkular-java-client/target/surefire-reports/testng-results.xml
/var/www/html/hawkular-test-results/rest-client-results.xml; cp
/home/hudson/hawkular-java-client/target/surefire-reports/emailable-
report.html /var/www/html/hawkular-test-results/rest-client-results.html\n\  
" >> /home/hudson/start.sh  
  
RUN chmod 766 /home/hudson/start.sh  
  
USER root  
WORKDIR /home/hudson  
CMD ["/usr/bin/supervisord"]  
  

