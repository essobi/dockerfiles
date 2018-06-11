FROM node  
EXPOSE 7000  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get -y install openjdk-7-jdk --no-install-recommends \  
&& npm install bower -g \  
&& echo '{ "allow_root": true }' > /root/.bowerrc \  
&& npm install -g grunt-cli \  
&& apt-get -y install wget --no-install-recommends \  
&& wget -q -O /usr/bin/lein
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein &&
chmod +x /usr/bin/lein && lein \  
&& apt-get remove -y wget \  
&& cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs.rename/fs.move/
./lib/utils/rename.js \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV APP_HOME /usr/local/visualreview  
ENV APP_TEMP_HOME /usr/local/visualreviewTemp  
  
# RUN mkdir -p ${APP_HOME}  
# RUN mkdir -p ${APP_TEMP_HOME}  
WORKDIR ${APP_TEMP_HOME}  
  
# add source  
ADD . ${APP_TEMP_HOME}  
  
RUN LEIN_ROOT=true lein uberjar \  
&& rm -fr /root/.cache /root/.lein /root/.m2 /root/.npm /root/.node-gyp \  
&& mkdir output \  
&& mv target/*-standalone.jar output \  
&& rm -fr target  
  
WORKDIR ${APP_HOME}  
RUN mv ${APP_TEMP_HOME}/output/*-standalone.jar ${APP_HOME} \  
&& cp ${APP_TEMP_HOME}/config.edn . \  
&& rm -fr $APP_TEMP_HOME \  
&& mv `ls *-standalone.jar` app-standalone.jar  
  
CMD ["java", "-jar", "app-standalone.jar"]  

