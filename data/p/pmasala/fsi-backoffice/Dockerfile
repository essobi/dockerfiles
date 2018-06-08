FROM pmasala/entando-base-image-432  
LABEL maintainer="Pietrangelo Masala <p.masala@entando.com>"  
  
COPY filter-development-unix.properties /opt/entando/filter-development-
unix.properties  
  
WORKDIR /opt/entando  
  
# Cloning the entando fsi-onboardind demo, injecting filter parameters and
patching permissions  
# for OpenShift deployment  
RUN git clone https://github.com/entando/fsi-onboarding-entando.git \  
&& rm -f fsi-onboarding-entando/fsi-backoffice/src/main/filters/filter-
development-unix.properties \  
&& cp filter-development-unix.properties fsi-onboarding-entando/fsi-
backoffice/src/main/filters/ \  
&& chmod -R 777 /opt/entando/fsi-onboarding-entando/fsi-backoffice/  
  
USER 1001  
WORKDIR /opt/entando/fsi-onboarding-entando/fsi-backoffice  
  
ENTRYPOINT [ "mvn", "-Dmaven.repo.local=/opt/entando/.m2/repository",
"jetty:run" ]  
  
EXPOSE 8080  

