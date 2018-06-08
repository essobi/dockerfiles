# OOI UI  
# <https://github.com/oceanzus/muframe.git>  
# Author: RPS ASA  
# Usage: <https://github.com/asascience-open/ooi-ui/wiki/Automated-
Deployment-(Docker)>  
FROM oceanzus/ooi-base-image  
MAINTAINER James D. Case <case@oceanz.org>  
  
# OOI UI Installation  
WORKDIR /root  
ADD git-deploy.sh /root/git-deploy.sh  
RUN /bin/bash -c "chmod +x /root/git-deploy.sh && /root/git-deploy.sh"  
  
RUN mkdir /root/muframe_data  
  
WORKDIR /root/muframe  
ENV WORKON_HOME /root/.virtualenvs  
RUN /bin/bash -c "source /root/.venvburrito/startup.sh \  
&& workon ooiui \  
&& pip install -r requirements.txt"  
  
ADD start_ooi-ui-muframe.sh /root/muframe/start_ooi-ui-muframe.sh  
RUN chmod +x /root/muframe/start_ooi-ui-muframe.sh  
  
EXPOSE 7090  
CMD [ "/bin/bash", "-c", "/root/muframe/start_ooi-ui-muframe.sh" ]

