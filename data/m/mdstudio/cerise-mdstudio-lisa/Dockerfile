FROM mdstudio/cerise:develop  
MAINTAINER Felipe Zapata <f.zapata@esciencecenter.nl>  
  
RUN apt-get update \  
&& apt-get install -y wget  
  
COPY api /home/cerise/api  
RUN chown -R cerise:cerise /home/cerise/api  
  
COPY known_hosts /home/cerise/.ssh/  
RUN chown -R cerise:cerise /home/cerise/.ssh/known_hosts  
  
# Download CWL Steps  
RUN mkdir /home/cerise/scripts  
COPY scripts/get_cwl_steps.sh /home/cerise/scripts  
RUN /home/cerise/scripts/get_cwl_steps.sh  

