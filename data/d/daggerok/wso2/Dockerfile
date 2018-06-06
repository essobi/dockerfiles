# docker build -t esb .  
# docker run --rm -it --name esb -p 9443:9443 -p 11111:11111 -p 8243:8243 -p
8280:8280 esb:latest  
# docker ps  
# open https://admin:admin@127.0.0.1:9443/carbon/  
# docker rm -v -f $(docker ps -a|grep -v CONTAINER|awk '{print $1}')  
FROM openjdk:8u131-jdk-alpine  
MAINTAINER Maksim Kostromin https://github.com/daggerok/docker  
  
ARG WSO2_ESB_USER="wso2-esb"  
ARG WSO2_ESB_VERSION="6.1.0"  
ARG DROPBOX_HASH="7j592kjmlnj7m3a"  
ARG WSO2_ESB_FILE_ARG="wso2ei-${WSO2_ESB_VERSION}"  
ARG
WSO2_ESB_URL_ARG="https://www.dropbox.com/s/${DROPBOX_HASH}/${WSO2_ESB_FILE_ARG}.zip"  
#ARG WSO2_ESB_URL_ARG="https://product-dist.wso2.com/products/enterprise-
integrator/${WSO2_ESB_VERSION}/${WSO2_ESB_FILE_ARG}.zip"  
ENV WSO2_ESB_URL=${WSO2_ESB_URL_ARG} \  
WSO2_ESB_FILE=${WSO2_ESB_FILE_ARG} \  
WSO2_ESB_USER_HOME="/home/${WSO2_ESB_USER}"  
ENV WSO2_ESB_HOME="${WSO2_ESB_USER_HOME}/${WSO2_ESB_USER}"  
RUN apk --no-cache --update add busybox-suid bash wget ca-certificates unzip
sudo openssh-client shadow \  
&& echo "${WSO2_ESB_USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& adduser -h ${WSO2_ESB_USER_HOME} -s /bin/bash -D -u 1025 ${WSO2_ESB_USER}
${WSO2_ESB_USER}-group \  
&& usermod -a -G wheel ${WSO2_ESB_USER} \  
&& apk --no-cache --no-network --purge del busybox-suid ca-certificates unzip
shadow \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
USER ${WSO2_ESB_USER}  
WORKDIR ${WSO2_ESB_USER_HOME}  
  
CMD /bin/bash  
EXPOSE 9443 8243 8280 11111  
ENTRYPOINT /bin/bash ${WSO2_ESB_FILE}/bin/integrator.sh  
  
RUN wget -q ${WSO2_ESB_URL} \  
&& unzip -q "${WSO2_ESB_FILE}.zip" \  
&& rm -rf "${WSO2_ESB_FILE}.zip"  
  
HEALTHCHECK \--timeout=2s --retries=22 \  
CMD wget -q --spider --no-check-certificate
https://127.0.0.1:9443/carbon/admin/login.jsp || exit 1  

