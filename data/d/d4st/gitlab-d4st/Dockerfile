# GitLab image configured for use in the DITA for Small Teams  
# system. Adds custom git hooks to the base image.  
#  
# Using the sameersbn version because it's better documented  
# and generally better organized than the office gitlab-ce  
# container.  
FROM sameersbn/gitlab:latest  
MAINTAINER Eliot Kimber "ekimber@contrext.com"  
COPY admin-scripts /var/opt/d4st/bin/  
RUN cd /var/opt/d4st && \  
wget https://github.com/dita-for-small-teams/dfst-git-commit-
hooks/archive/develop.zip && \  
unzip develop.zip && \  
rm develop.zip && \  
mv dfst-git-commit-hooks-develop/server-side custom_hooks && \  
cd /var/opt/d4st/bin && \  
chmod a+x *  
  
ENV PATH ${PATH}:/var/opt/d4st/bin  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["app:start"]  
#  
# End of Docker file  
#  

