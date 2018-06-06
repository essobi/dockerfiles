FROM shastafareye/bash  
# IMAGE mazaclub/coind-trigger  
RUN echo "This just waits for mazaclub/coind-base to be (hopefully) finished"
\  
&& echo "before completing this build in order to trigger App builds," \  
&& echo "like Encompass-Mercury builds on dockerhub"  
RUN x=0; while [ $x != 15 ] ; do sleep 60 ; x=$((x+1)) ; echo "Waited $x
minutes" ; done \  
&& echo "Done"  
RUN touch /done  
  

