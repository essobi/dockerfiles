FROM cloudfoundry/cflinuxfs2  
MAINTAINER Leandro David Cacciagioni <leandro.21.2008@gmail.com>  
  
# Here we try to declare all the env vars that the DEA normally expose  
# For VCAP_APPLICATION we have used the info provided in
http://docs.run.pivotal.io/devguide/deploy-apps/environment-variable.html as
of 03/31/2015  
ENV DEBIAN_FRONTEND=noninteractive PORT=8080 VCAP_APP_PORT=8080
HOME=/home/vcap/app PWD=/home/vcap USER=vcap TMPDIR=/home/vcap/tmp
VCAP_APP_HOST=0.0.0.0
VCAP_APPLICATION='{"instance_id":"451f045fd16427bb99c895a2649b7b2a","instance_index":0,"host":"0.0.0.0","port":8080,"started_at":"2013-08-12
00:05:29 +0000","started_at_timestamp":1376265929,"start":"2013-08-12 00:05:29
+0000","state_timestamp":1376265929,"limits":{"mem":512,"disk":1024,"fds":16384}
,"application_version":"c1063c1c-40b9-434e-a797-db240b587d32","application_name":"styx-
james","application_uris":["styx-james.a1-app.cf-
app.com"],"version":"c1063c1c-40b9-434e-a797-db240b587d32","name":"styx-
james","uris":["styx-james.a1-app.cf-app.com"],"users":null}'
CF_INSTANCE_ADDR=1.2.3.4:8080 CF_INSTANCE_INDEX=0 CF_INSTANCE_IP=1.2.3.4
CF_INSTANCE_PORT=8080 CF_INSTANCE_PORTS=[{external:8080,internal:8080}]
VCAP_SERVICES='{}' CF_STACK=cflinuxfs2  
  
ENTRYPOINT /entrypoint.sh  
# Here we try to expose the default port  
EXPOSE 8080  
  
# We set the default working dir to the place where your app is  
WORKDIR /home/vcap/app  
# Here we add our code  
ADD entrypoint.sh /entrypoint.sh  
  
RUN mkdir /home/vcap/tmp && chmod 755 /entrypoint.sh  

