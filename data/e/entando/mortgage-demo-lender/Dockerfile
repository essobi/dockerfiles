FROM entando/mortgage-base-image  
  
LABEL maintainer="Pietrangelo Masala <p.masala@entando.com>" \  
io.k8s.description="Entando lender image for the mortgage demo" \  
io.k8s.display-name="Entando lender image mortgage-demo 1.0" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="mortgage,entando,bpms."  
  
ENV ENTANDO_MORTGAGE_LENDER=1.0  
  
WORKDIR /opt/entando  
  
COPY entando-lender/ /opt/entando/entando-lender/  
  
USER root  
  
RUN chmod -R 777 /opt/entando/entando-lender/  
  
USER 1001  
  
WORKDIR /opt/entando/entando-lender  
  
ENTRYPOINT [ "mvn", "-Dmaven.repo.local=/opt/entando/.m2/repository",
"jetty:run" ]  
  
EXPOSE 8080

