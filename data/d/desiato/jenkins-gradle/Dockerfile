FROM jenkins/jenkins  
  
ENV SDKMAN_DIR /usr/share/sdkman/dir  
  
USER root  
ADD jenkins-gradle.sh /usr/local/bin/  
ENTRYPOINT ["/sbin/tini", "--", "jenkins-gradle.sh"]  
RUN apt-get update && apt-get install -y zip && rm -rf /var/lib/apt/lists/* \  
&& mkdir -p "$(dirname "$SDKMAN_DIR")" \  
&& chown -R jenkins: "$(dirname "$SDKMAN_DIR")"  
  
USER jenkins  
SHELL ["/bin/bash", "-c"]  
RUN curl -s "https://get.sdkman.io" | bash \  
&& source "$SDKMAN_DIR/bin/sdkman-init.sh" \  
&& sdk install gradle \  
&& /usr/local/bin/install-plugins.sh git gradle workflow-aggregator pipeline-
utility-steps active-directory  

