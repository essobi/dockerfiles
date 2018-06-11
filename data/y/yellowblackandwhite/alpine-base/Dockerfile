FROM alpine  
MAINTAINER Pavel Litvinenko <plitvinenko@molodejj.tv>  
USER root  
# Timezone and locale  
ENV TIMEZONE Europe/Moscow  
ENV TZ Europe/Moscow  
# Set Workdir  
VOLUME ["/src", "/logs", "/data", "/default", "/scripts"]  
WORKDIR /src  
# Install common packages  
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories; \  
apk upgrade && apk update && \  
apk add --update sudo bash dbus curl ca-certificates openssl \  
openssh-client sshpass tar unzip bash coreutils tzdata && \  
adduser -D alpine && \  
bash -c 'echo "alpine ALL=(ALL:ALL) NOPASSWD:ALL" | (EDITOR="tee -a" visudo)'
&& \  
chmod 777 /src && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
echo "ipv6" >> /etc/modules  
# Generate ssh key  
RUN dbus-uuidgen > /etc/machine-id && \  
ssh-keygen -f ~/.ssh/id_rsa -t rsa -N '' && \  
cat ~/.ssh/id_rsa.pub  
# Install consul-template  
ENV CONSUL_TEMPLATE_VERSION 0.18.1  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /tmp/  
RUN unzip /tmp/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -d
/tmp/ && \  
mv /tmp/consul-template /usr/local/bin/consul-template && \  
rm -rf /tmp/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
mkdir -p /consul-template /consul-template/config.d /consul-template/templates  
COPY entry_point.sh /  
ENTRYPOINT ["/entry_point.sh"]  
# Change user  
USER alpine  

