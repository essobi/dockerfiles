FROM anigeo/awscli  
  
ADD https://raw.githubusercontent.com/colinbjohnson/aws-missing-
tools/master/ec2-automate-backup/ec2-automate-backup.sh /bin/ec2-automate-
backup  
ADD entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /bin/ec2-automate-backup /entrypoint.sh && \  
apk add --update bash && rm -rf /var/cache/apk/*  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

