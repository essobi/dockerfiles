FROM ymonnier/sdkman-java  
  
SHELL [ "/bin/bash", "-c" ]  
  
RUN source /root/.sdkman/bin/sdkman-init.sh && sdk install java  
RUN source /root/.sdkman/bin/sdkman-init.sh && sdk install kotlin  
RUN source /root/.sdkman/bin/sdkman-init.sh && sdk install kscript  
  
ENTRYPOINT [ "/usr/bin/env", "kscript" ]  
CMD [ "--help" ]  
  

