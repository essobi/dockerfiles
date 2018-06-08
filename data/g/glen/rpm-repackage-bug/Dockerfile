FROM glen/pld  
  
RUN echo CREATING SCENARIO, IGNORE ALL THE NOISE, SKIP TO "SCENARIO CREATED"
STEP  
# install pam, older version  
RUN poldek -n th-2015 -u pam --noask --downgrade  
  
# make changes to config file  
RUN echo >> /etc/environment  
# 1. upgrade pam 1.1 -> 1.2  
RUN poldek -u pam  
# 2. downgrade, this does goes well (no changes to config files)  
RUN rpm -Uv --downgrade /var/spool/repackage/*/pam*.rpm  
  
# running this command will make reproducer fail (not reproduce problem)  
#RUN rm -rv /var/spool/repackage/*  
# 3. upgrade again (to produce multiple repackage files)  
RUN poldek -u pam  
  
# 4. downgrade matching multiple pam packages  
RUN echo SCENARIO CREATED, RUNNING THE ACTUAL REPRODUCER  
RUN ls -l /var/spool/repackage/*/pam*.rpm  
RUN rpm -Uv --downgrade /var/spool/repackage/*/pam*.rpm -vv || :  

