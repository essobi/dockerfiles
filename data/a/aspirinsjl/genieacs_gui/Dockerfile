FROM aspirinsjl/genieacs  
  
# To use 'source' via bash  
# RUN rm /bin/sh && \  
# ln -s /bin/bash /bin/sh  
  
EXPOSE 7547 3000  
  
RUN /bin/bash -c "gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \  
\curl -sSL https://get.rvm.io | bash -s stable --rails && \  
source /etc/profile.d/rvm.sh && \  
git clone https://github.com/zaidka/genieacs-gui.git /opt/git/genieacs-gui &&
\  
cd /opt/git/genieacs-gui && \  
cp config/graphs-sample.json.erb config/graphs.json.erb && \  
cp config/index_parameters-sample.yml config/index_parameters.yml && \  
cp config/summary_parameters-sample.yml config/summary_parameters.yml && \  
cp config/parameters_edit-sample.yml config/parameters_edit.yml && \  
cp config/parameter_renderers-sample.yml config/parameter_renderers.yml && \  
cp config/roles-sample.yml config/roles.yml && \  
cp config/users-sample.yml config/users.yml && \  
bundle"

