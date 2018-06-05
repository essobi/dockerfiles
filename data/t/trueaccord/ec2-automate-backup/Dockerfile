FROM python:2.7  
RUN pip install awscli  
  
RUN git clone https://github.com/colinbjohnson/aws-missing-tools.git /opt/aws-
missing-tools  
  
ENTRYPOINT ["/opt/aws-missing-tools/ec2-automate-backup/ec2-automate-
backup.sh"]  
  

