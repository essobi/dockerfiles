FROM entando/mortgage-base-image  
  
LABEL maintainer="Pietrangelo Masala <p.masala@entando.com>" \  
io.k8s.description="Entando applicant image for the mortgage demo" \  
io.k8s.display-name="Entando applicant image mortgage-demo 1.0" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="mortgage,entando,bpms."  
  
ENV ENTANDO_MORTGAGE_APPLICANT=1.0  
  
WORKDIR /opt/entando  
  
COPY entando-applicant/ /opt/entando/entando-applicant/  
  
USER root  
  
RUN chmod -R 777 /opt/entando/entando-applicant/  
  
USER 1001  
  
WORKDIR /opt/entando/entando-applicant  
  
ENTRYPOINT [ "mvn", "-Dmaven.repo.local=/opt/entando/.m2/repository",
"jetty:run" ]  
  
EXPOSE 8080  

