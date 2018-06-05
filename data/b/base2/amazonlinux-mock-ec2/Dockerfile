FROM amazonlinux:2016.09  
#Make me a close a possible to an Amazon Linux EC2 AMI as possible  
COPY packages.txt /root/packages.txt  
RUN yum -y install $(cat /root/packages.txt)  
  
# deploy and enable a mock ec2 metadata service  
COPY aws-mock-metadata/ /opt/aws-mock-metadata/  
RUN ln -fs /opt/aws-mock-metadata/service.init /etc/init.d/aws-mock-metadata
&& \  
chkconfig aws-mock-metadata on  
  
ENV AVAILABILITY_ZONE="ap-southeast-2a"  
ENV INSTANCE_ID="i-01e0f26d68ca3ab48"  
ENV AWS_SESSION_TOKEN=""  
ENV HOSTNAME="ip-172-17-0-1.ap-southeast-2.compute.internal"  
ENV PRIVATE_IP="10.0.0.10"  
ENV ROLE_ARN=""  
ENV ROLE_NAME=""  
ENV VPC_ID="vpc-abcdef99"  
CMD "/sbin/init"  

