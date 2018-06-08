FROM lightjason/agentspeak  
  
# --- configuration section ----------------------  
ENV DOCKERIMAGE_BENCHMARK_VERSION simulation  
  
  
# --- machine configuration section --------------  
RUN git clone https://github.com/SigmaAlphaPi/sap_ba_thesis.git
/tmp/sim_scenario  
RUN cd /tmp/sim_scenario && git checkout $DOCKERIMAGE_BENCHMARK_VERSION  
RUN cd /tmp/sim_scenario && mvn install -DskipTests  
  
RUN mkdir -p /root/bin  
RUN cd /tmp/sim_scenario && export JAR=$(mvn -B help:evaluate
-Dexpression=project.build.finalName | grep -vi info | grep -ivvv "warning")
&& mv target/$JAR.jar /root/bin  
RUN cd /tmp/sim_scenario && export JAR=$(mvn -B help:evaluate
-Dexpression=project.build.finalName | grep -vi info | grep -ivvv "warning")
&& echo -e "#!/bin/sh -e\\\nSRC=\$(dirname \$0)\\\njava -jar \$JAVA_OPTS
\$SRC/$JAR.jar \$@" > /root/bin/sim_scenario  
RUN chmod a+x /root/bin/sim_scenario  
  
RUN rm -rf /tmp/*  
ENV PATH /root/bin:$PATH  

