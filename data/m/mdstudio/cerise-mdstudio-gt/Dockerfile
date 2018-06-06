FROM mdstudio/cerise:0.1.0  
MAINTAINER Felipe Zapata <f.zapata@esciencecenter.nl>  
  
RUN apt-get update && apt-get install -y wget  
  
COPY api /home/cerise/api  
RUN chown -R cerise:cerise /home/cerise/api  
  
COPY known_hosts /home/cerise/.ssh/  
RUN chown -R cerise:cerise /home/cerise/.ssh/known_hosts  
  
# Download CWL Steps  
RUN wget https://raw.githubusercontent.com/MD-Studio/cerise-mdstudio-share-
data/v0.1/scripts/get_cwl_steps.sh -P /home/cerise/scripts  
RUN chmod u+x /home/cerise/scripts/get_cwl_steps.sh  
RUN /home/cerise/scripts/get_cwl_steps.sh  

