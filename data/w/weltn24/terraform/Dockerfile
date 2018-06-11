FROM alpine:3.3  
MAINTAINER adam.vincze@welt.de  
  
RUN apk update &&\  
apk add openssl  
  
RUN mkdir /tf &&\  
wget
"https://releases.hashicorp.com/terraform/0.6.11/terraform_0.6.11_linux_amd64.zip"
-O tf.zip &&\  
unzip tf.zip -d /tf &&\  
rm /tf/terraform-provider-atlas \  
/tf/terraform-provider-azure \  
/tf/terraform-provider-azurerm \  
/tf/terraform-provider-chef \  
/tf/terraform-provider-cloudflare \  
/tf/terraform-provider-cloudstack \  
/tf/terraform-provider-consul \  
/tf/terraform-provider-digitalocean \  
/tf/terraform-provider-dme \  
/tf/terraform-provider-dnsimple \  
/tf/terraform-provider-google \  
/tf/terraform-provider-heroku \  
/tf/terraform-provider-mailgun \  
/tf/terraform-provider-mysql \  
/tf/terraform-provider-openstack \  
/tf/terraform-provider-postgresql \  
/tf/terraform-provider-powerdns \  
/tf/terraform-provider-rundeck \  
/tf/terraform-provider-statuscake \  
/tf/terraform-provider-vcd \  
/tf/terraform-provider-vsphere \  
/tf.zip  
ENV PATH /tf/:$PATH  
  
COPY ca-certificates.crt /etc/ssl/certs/ca-certificates.crt  
  
  
  

