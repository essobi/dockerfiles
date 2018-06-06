# Consul-template  
FROM debian  
  
MAINTAINER Yury Kavaliou <Yury_Kavaliou@epam.com>  
  
ENV BIN_PATH /usr/local/bin  
  
ADD https://github.com/hashicorp/consul-
template/releases/download/v0.10.0/consul-template_0.10.0_linux_amd64.tar.gz
/tmp/consul-template.tar.gz  
RUN tar -xf /tmp/consul-template.tar.gz \  
&& mv consul-template_0.10.0_linux_amd64/consul-template /bin/consul-template
\  
&& chmod a+x /bin/consul-template  
  
COPY ./files/init_template.sh $BIN_PATH/init_template.sh  
COPY ./files/update_vip.sh $BIN_PATH/update_vip.sh  
COPY ./files/update_vip.ctmpl $BIN_PATH/update_vip.ctmpl  
  
RUN chmod u+x $BIN_PATH/update_vip.sh \  
$BIN_PATH/init_template.sh  
  
ENTRYPOINT ["/usr/local/bin/init_template.sh"]

