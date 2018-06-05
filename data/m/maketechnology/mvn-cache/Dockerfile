#FROM maketechnology/jdk:8-mvn-git  
FROM maketechnology/jdk:8-ubu-mvn-git  
  
RUN apt-get update -y && apt-get install -y --no-install-recommends xvfb
metacity \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY token /token  
COPY settings.xml /settings.xml  
#RUN dbus-uuidgen > /var/lib/dbus/machine-id  
  
RUN mkdir /m2 \  
&& git clone https://gitlab-ci-token:$(cat /token)@gitlab.com/gzunino/dbt2.git
/src \  
&& cd /src \  
&& mvn -B -fae -s /settings.xml clean verify -f pom.xml
-Dmaven.test.failure.ignore=true -Pmodules,products,envs \  
&& mvn -B -fn -s /settings.xml dependency:resolve
-P!modules,default,uiTests,report \  
&& mvn -B -s /settings.xml clean verify -fn -Dmaven.test.failure.ignore=true
-Dproduct.dir=../com.querix.dbt.product/target/products/com.querix.dbt.dbtstudio/linux/gtk/x86_64/
-Dproduct.from.dir=true -P!modules,default,uiTests,report \  
&& rm -rf /tmp/* \  
&& rm -rf /src \  
&& rm -rf ~/.swt \  
&& rm -f /token  

