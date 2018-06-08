FROM orconano/docker-sdkman  
  
RUN mkdir /app  
WORKDIR /app  
CMD ["grails"]  
  
COPY settings.groovy /root/.grails/settings.groovy  
  
# install newest version of the 2.5.x branch  
RUN sdkman-wrapper.sh install grails 2.5.1 && sdkman-wrapper.sh flush archives
&& sdkman-exec.sh grails help  

