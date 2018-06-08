FROM getdtk/baseimage:0.18  
MAINTAINER dduvnjak <dario@atlantbh.com>  
  
ENV tenant_user=dtk1  
  
RUN useradd -ms /bin/bash ${tenant_user} && \  
mkdir -p /home/${tenant_user}/server && \  
mkdir -p /home/${tenant_user}/.ssh  
COPY . /home/${tenant_user}/server/current  
  
WORKDIR /home/${tenant_user}/server/current  
  
RUN bash docker/serverbuild/install.sh  
  
EXPOSE 2222  
EXPOSE 6163  
EXPOSE 80  
CMD ["/addons/init.sh"]  

