FROM giorgioazzinnaro/openmrs-platform:2.0.5  
LABEL maintainer giorgio.azzinnaro@gmail.com  
  
# Copy the modules over  
ADD referenceapplication-package-2.6.0 /root/referenceapplication  
RUN mkdir -p /root/.OpenMRS/modules \  
&& mv /root/referenceapplication/* /root/.OpenMRS/modules/ \  
&& rm -rf /root/referenceapplication  
  
# This now contains modules  
VOLUME /root/.OpenMRS  

