FROM rroemhild/ejabberd  
  
ENV XMPP_DOMAIN=mongol.chat \  
EJABBERD_STARTTLS=false \  
# EJABBERD_HTTPS=false \  
EJABBERD_ADMINS=admin@mongol.chat \  
EJABBERD_USERS=admin@mongol.chat:admin \  
EJABBERD_MOD_ADMIN_EXTRA=true \  
EJABBERD_CONFIGURE_ODBC=true \  
EJABBERD_ODBC_TYPE=mysql \  
EJABBERD_ODBC_SERVER=172.17.0.2 \  
EJABBERD_ODBC_DATABASE=chat \  
EJABBERD_ODBC_USERNAME=root \  
EJABBERD_ODBC_PASSWORD=root \  
EJABBERD_AUTH_METHOD=external \  
EJABBERD_EXTAUTH_PROGRAM=$EJABBERD_HOME/auth/auth.sh \  
EJABBERD_EXTAUTH_INSTANCES=3 \  
EJABBERD_EXTAUTH_CACHE=false \  
EJABBERD_SKIP_MODULES_UPDATE=true \  
EJABBERD_SOURCE_MODULES=mod_contact_sync\ mod_offline_msg\ mod_rmq_client \  
# EJABBERD_CONTRIB_MODULES=mod_log_chat \  
AUTH_HOST=http://172.17.0.5 \  
EJABBERD_RMQ_HOST=rabbitmq \  
EJABBERD_RMQ_USERNAME=guest \  
EJABBERD_RMQ_PASSWORD=guest \  
EJABBERD_RMQ_PORT=5672 \  
EJABBERD_RMQ_VHOST=\/  
  
RUN mkdir $EJABBERD_HOME/auth  
  
ADD ./auth $EJABBERD_HOME/auth  
ADD ./modules $EJABBERD_HOME/module_source  
USER root  
RUN chown -R $EJABBERD_USER: $EJABBERD_HOME  
RUN chmod a+x -R $EJABBERD_HOME/auth  
ADD ./docker/ejabberd.yml.tpl /opt/ejabberd/conf/ejabberd.yml.tpl  
ADD ./docker/ejabberdctl.cfg.tpl /opt/ejabberd/conf/ejabberdctl.cfg.tpl  
  
USER $EJABBERD_USER  
VOLUME ["$EJABBERD_HOME/auth", "$EJABBERD_HOME/module_source"]  
  
  
  

