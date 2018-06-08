# OOI UI Services  
# <https://github.com/oceanzus/ooi-ui-deployments.git>  
# Author: RPS ASA  
# Usage: <https://github.com/asascience-open/ooi-ui/wiki/Automated-
Deployment-(Docker)>  
FROM oceanzus/ooi-base-image  
MAINTAINER James D. Case <case@oceanz.org>  
  
# OOI UI Installation  
WORKDIR /root  
ADD git-deploy.sh /root/git-deploy.sh  
RUN /bin/bash -c "chmod +x /root/git-deploy.sh && /root/git-deploy.sh"  
  
WORKDIR /root/ooi-ui-services  
ENV WORKON_HOME /root/.virtualenvs  
RUN /bin/bash -c "source /root/.venvburrito/startup.sh \  
&& workon ooiui \  
&& pip install -r ./ooiservices/requirements/common.txt"  
  
ADD start_ooi-ui-services.sh /root/ooi-ui-services/start_ooi-ui-services.sh  
RUN chmod +x /root/ooi-ui-services/start_ooi-ui-services.sh  
  
EXPOSE 4000  
CMD [ "/bin/bash", "-c", "/root/ooi-ui-services/start_ooi-ui-services.sh" ]  

