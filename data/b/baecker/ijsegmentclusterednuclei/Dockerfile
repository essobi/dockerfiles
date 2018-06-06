FROM baecker/fiji-base:latest  
  
RUN cd plugins && wget -O imagescience.jar
https://imagescience.org/meijering/software/download/imagescience.jar  
RUN cd plugins && wget -O FeatureJ_.jar
https://imagescience.org/meijering/software/download/FeatureJ_.jar  
  
RUN cd /fiji/macros && wget -O IJSegmentClusteredNuclei.ijm
https://gist.githubusercontent.com/volker-
baecker/d1c973c9b8e60afa537206f515f89964/raw/c0b395222afe47bbaabfea374560ecd6b8e983d1/IJSegmentClusteredNuclei.ijm  
RUN cd /fiji && wget -O run-segment-clustered-nuclei.sh
https://gist.githubusercontent.com/volker-
baecker/dd6544ed91d940224df48192dd2cc947/raw/bf7507def2dc9ff1df793e0d4454c2999a65f082/run-
segment-clustered-nuclei.sh && chmod a+x run-segment-clustered-nuclei.sh  
  
ENTRYPOINT ["/bin/sh", "run-segment-clustered-nuclei.sh"]  

