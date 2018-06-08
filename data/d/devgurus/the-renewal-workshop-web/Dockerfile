FROM devgurus/sunrise-base  
  
ENV LC_ALL "en_US"  
ENV LANG "en_US"  
# npm needed for buildModules  
WORKDIR /tmp/repo  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && apt-get install
-y nodejs  
RUN curl -sL https://npmjs.org/install.sh | sh  
  
# Install rvm (i.e. ruby)  
RUN apt-get update && apt-get install ruby -y  
RUN ruby -v  
  
RUN npm install -g grunt  
RUN gem install sass  
  
ADD . .  
RUN ["./activator", "buildModules"]  
RUN ["./activator", "universal:packageZipTarball"]  
  
WORKDIR target/universal  
  
RUN tar -xf commercetools-sunrise-*  
RUN mv commercetools-sunrise-*/ /opt/sunrise  
  
# Cleanup  
WORKDIR /opt/sunrise  
RUN rm -r /tmp/repo  
  
# Install datadog agent  
ADD entrypoint.sh .  
RUN DD_API_KEY='dd_api_key' DD_INSTALL_ONLY=true bash -c "$(curl -L
https://raw.githubusercontent.com/DataDog/dd-agent/master/packaging/datadog-
agent/source/install_agent.sh)"  
RUN chmod +x entrypoint.sh  
  
# Make footprint smaller  
RUN apt-get purge -y nodejs ruby && apt-get -y autoremove  
  
ENTRYPOINT ["./entrypoint.sh", "./bin/commercetools-sunrise"]  

