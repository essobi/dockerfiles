FROM amazonlinux:2017.03  
RUN yum update -y && yum install -y awslogs && yum clean all  
  
ENV AWS_CONFIG_FILE /etc/awslogs/awscli.conf  
  
RUN sed -i '/region =/d' /etc/awslogs/awscli.conf  
  
ENTRYPOINT ["/usr/bin/aws", "logs", "push"]  

