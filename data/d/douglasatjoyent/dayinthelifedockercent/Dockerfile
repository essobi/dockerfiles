FROM centos  
  
RUN yum install -y openssl docker java-1.8.0-openjdk git which  
RUN curl -o jmeter.tgz http://www-eu.apache.org/dist//jmeter/binaries/apache-
jmeter-3.3.tgz  
RUN tar -zxvf jmeter.tgz  
env JMETER_BIN /apache-jmeter-3.3/bin  
  
ENV PATH $PATH:$JMETER_BIN  
  
RUN git clone https://github.com/douglasAtJoyent/DayInTheLifeOfTriton  
  
RUN ssh-keygen -t rsa -f ~/.ssh/sdc_docker_jmeter_id_rsa -b 2048 -N ""  
RUN curl -O https://raw.githubusercontent.com/joyent/sdc-
docker/master/tools/sdc-docker-setup.sh  
RUN chmod 777 sdc-docker-setup.sh  
ENV PUBLIC_KEY=/root/.ssh/sdc_docker_jmeter_id_rsa.pub  
ENV PRIVATE_KEY=/root/.ssh/sdc_docker_jmeter_id_rsa  
ENV TEST_NAME=/DayInTheLifeOfTriton/JMeter/DayInTheLifeUnified.jmx  
ENV PATH=$PATH:/apache-jmeter-3.3/bin  
ENTRYPOINT bash  
  

