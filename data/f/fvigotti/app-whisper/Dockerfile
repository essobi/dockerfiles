FROM fvigotti/env-fatubuntu  
  
env STABLE_WHISPER_BRANCH 0.9.13  
env STABLE_CARBON_BRANCH 0.9.12  
# install whisper  
RUN git clone \--depth 1 -b ${STABLE_WHISPER_BRANCH}
https://github.com/graphite-project/whisper.git /opt/whisper_stable  
RUN git clone \--depth 1 https://github.com/graphite-project/whisper.git
/opt/whisper_live  
  
# install carbon  
RUN git clone \--depth 1 -b ${STABLE_CARBON_BRANCH}
https://github.com/graphite-project/carbon.git /opt/carbon_stable  
RUN git clone \--depth 1 https://github.com/graphite-project/carbon.git
/opt/carbon_live  
  
VOLUME /opt/whisper_live  
VOLUME /opt/whisper_stable  
  
VOLUME /opt/carbon_live  
VOLUME /opt/carbon_stable  
  

