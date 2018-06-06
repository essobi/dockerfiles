# This is the docker hub image  
FROM pmasala/entando-base-image-432  
LABEL maintainer="Pietrangelo Masala <p.masala@entando.com>"  
  
COPY filter-development-unix.properties /opt/entando/filter-development-
unix.properties  
  
WORKDIR /opt/entando  
  
RUN git clone https://github.com/entando/fsi-onboarding-entando.git \  
&& rm -f fsi-onboarding-entando/fsi-customer/src/main/filters/filter-
development-unix.properties \  
&& cp filter-development-unix.properties fsi-onboarding-entando/fsi-
customer/src/main/filters/ \  
&& chmod -R 777 /opt/entando/fsi-onboarding-entando/fsi-customer/  
  
USER 1001  
WORKDIR /opt/entando/fsi-onboarding-entando/fsi-customer  
  
ENTRYPOINT [ "mvn", "-Dmaven.repo.local=/opt/entando/.m2/repository",
"jetty:run" ]  
  
EXPOSE 8080  

