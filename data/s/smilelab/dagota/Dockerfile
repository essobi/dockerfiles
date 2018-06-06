from openshift/base-centos7  
  
LABEL authors="Patrice FERLET <patrice.ferlet@smile.fr"  
  
COPY ./ /usr/src/go/dagota/  
RUN set -xe; \  
cd /usr/src/go/dagota; \  
yum install -y golang; \  
go build; \  
mv dagota /usr/bin/dagota; \  
yum remove -y golang; \  
yum clean all;  
  
ENV DYN_TOKEN="123456789" DYN_RACK="rack1" DYN_DC="dc1" DYN_SVC=""  
EXPOSE 8080 8101  
ENTRYPOINT ["dagota"]  

