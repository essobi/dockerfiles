#  
# Copyright (c) 2001-2018 Primeton Technologies, Ltd.  
# All rights reserved.  
#  
# author: ZhongWen Li (mailto:lizw@primeton.com)  
#  
FROM primetoninc/jre:1.8  
  
LABEL maintainer="lizw@primeton.com" \  
provider="Primeton Technologies, Ltd."  
  
ENV APP_HOME="/app" \  
SERVER_PORT=8080 \  
DEBUG_PORT=8888 \  
DEBUG_ENABLE="no" \  
JAVA_VM_MEM_MIN=512 \  
JAVA_VM_MEM_MAX=1024  
  
# EXPOSE ${SERVER_PORT}  
ADD resources/entrypoint.sh ${APP_HOME}/bin/  
  
# maven build artifact  
# FROM this image can execute ONBUILD  
# ONBUILD ADD target/*.jar ${APP_HOME}/lib/  
# ONBUILD ADD src/main/resources/application.yml ${APP_HOME}/conf/  
# ONBUILD ADD src/main/resources/application.properties ${APP_HOME}/conf/  
  
ONBUILD EXPOSE ${SERVER_PORT}  
RUN chmod +x ${APP_HOME}/bin/entrypoint.sh \  
&& mkdir -p ${APP_HOME}/conf \  
&& echo "# Application Configuration directory" > ${APP_HOME}/conf/README.md  
  
ENTRYPOINT ["/bin/bash", "-c", "${APP_HOME}/bin/entrypoint.sh"]  

