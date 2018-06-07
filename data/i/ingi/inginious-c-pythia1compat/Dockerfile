# DOCKER-VERSION 1.1.0  
FROM ingi/inginious-c-base  
LABEL org.inginious.grading.name="pythia1compat"  
  
# Install Oz  
RUN yum -y install tcl tk boost  
  
ADD . /mozartRPM  
  
RUN rpm -ivh
/mozartRPM/mozart2-2.0.0-alpha.0+build.4091.61fe075-dirty-x86_64-linux.rpm  
  
# Environment variables  
RUN echo "export OZHOME=/opt/mozart2" >> /etc/profile.d/oz.sh && \  
echo "export PATH=/opt/mozart2/bin:$""PATH" >> /etc/profile.d/oz.sh  
  
# Replacing default INGInious  
RUN yes | cp -rf /mozartRPM/INGInious /bin/INGInious  
  
# Clean directories  
RUN rm -rf /mozartRPM  

