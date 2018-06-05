FROM alpine  
RUN apk add --update ansible py-boto  
ADD
https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py
/etc/ansible/ec2.py  
ADD
https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini
/etc/ansible/ec2.ini  
ENV ANSIBLE_HOSTS=/etc/ansible/ec2.py  
ENV EC2_INI_PATH=/etc/ansible/ec2.ini  
WORKDIR /app  
ENTRYPOINT ["ansible"]  
CMD ["--help"]  

