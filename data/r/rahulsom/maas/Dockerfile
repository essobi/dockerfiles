FROM rahulsom/docker-java:7u55  
  
MAINTAINER Rahul Somasunderam  
  
RUN yum install -y tar unzip  
  
WORKDIR /opt  
  
RUN wget -q
http://deploy.certifydatasystems.com/cdsng/rahul/LOINC_248_Text.zip && \  
mkdir loinc && \  
cd loinc && \  
unzip ../LOINC_248_Text.zip  
  
RUN wget -q
http://www.fda.gov/downloads/Drugs/DevelopmentApprovalProcess/UCM070838.zip &&
\  
mkdir ndc && \  
cd ndc && \  
unzip ../UCM070838.zip && \  
cat package.txt | tr '\t' ' ' | cut -d " " -f1 | sort | uniq > package-
product-ids.txt && \  
cat product.txt | tr '\t' ' ' | cut -d ' ' -f1 | sort | uniq > product-
product-ids.txt && \  
diff -y --suppress-common-lines package-product-ids.txt product-product-
ids.txt | uniq > ndc-diff.txt  
  
RUN wget -q
https://www.cms.gov/Medicare/Coding/ICD9ProviderDiagnosticCodes/Downloads/ICD-9-CM-v32-master-
descriptions.zip && \  
mkdir icd9 && \  
cd icd9 && \  
unzip ../ICD-9-CM-v32-master-descriptions.zip  
  
RUN source ~/.bashrc && \  
wget -q --no-check-certificate
https://github.com/rahulsom/maas/archive/master.tar.gz && \  
tar xzvf master.tar.gz && \  
cd maas-master && \  
./grailsw compile  
  
EXPOSE 8080  
VOLUME ["/opt/maas-master/data"]  
  
WORKDIR /opt/maas-master  
  
ENTRYPOINT source ~/.bashrc && \  
./grailsw run-script userScripts/Dataload.groovy && \  
./grailsw run-app  

