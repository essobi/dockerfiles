FROM openjdk:8-jdk-alpine  
  
ENV LEGATO_SPM_VERSION 15  
RUN apk add --no-cache wget && \  
mkdir -p -m 777 /legato-spm && \  
wget http://updatesite.sierrawireless.com/legato-spm/product/legato-
spm.$LEGATO_SPM_VERSION.zip -O /legato-spm/legato-spm.zip && \  
cd /legato-spm && \  
unzip -q legato-spm.zip && \  
rm legato-spm.zip  
  
ENTRYPOINT [ "/legato-spm/legato-spm" ]  

