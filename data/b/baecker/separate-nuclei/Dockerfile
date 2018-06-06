FROM baecker/fiji-base:latest  
  
RUN cd /fiji/macros && \  
wget -O separate_nuclei.ijm \  
https://gist.githubusercontent.com/volker-
baecker/627885ea40320e047f8b88f2888673af/raw/2270c2e33d2e09ffa5c41e7e438e9977f1cbd9d6/separate_nuclei.ijm  
RUN cd /fiji && \  
wget -O run_separate_nuclei.sh \  
https://gist.githubusercontent.com/volker-
baecker/1f2c03de203fe559068d9379b0a730bf/raw/5833c3537307eaf7015b3fedf8f1f1bb2e46c88c/run_separate_nuclei.sh
&& \  
chmod a+x run_separate_nuclei.sh  
ENTRYPOINT ["/bin/sh", "run_separate_nuclei.sh"]  

