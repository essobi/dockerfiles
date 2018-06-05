# How to execute:  
# $ docker build -t fiware-aiakos-unittests .  
# $ docker run --name fiware-aiakos-unittests fiware-aiakos-unittests  
FROM centos  
RUN curl --silent --location https://rpm.nodesource.com/setup | bash  
RUN yum update; yum -y install git gcc-c++ make nodejs rpm-build initscripts
crontabs  
RUN git clone https://github.com/telefonicaid/fiware-aiakos /opt/fiware-aiakos  
WORKDIR /opt/fiware-aiakos  
RUN npm install -g grunt-cli; npm install; ./node_modules/.bin/grunt test; sed
-i 's/production/development/' Gruntfile.js  
COPY sonar-project.properties sonar-project.properties  
CMD ./node_modules/.bin/grunt test; grunt lint-report test-report coverage-
report  

