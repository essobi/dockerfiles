FROM centos:7.4.1708  
  
ARG SU_EXEC_VERSION=0.2  
ARG SU_EXEC_URL="https://github.com/ncopa/su-
exec/archive/v${SU_EXEC_VERSION}.tar.gz"  
  
RUN yum install -y -q gcc make \  
&& curl -sL "${SU_EXEC_URL}" | tar -C /tmp -zxf - \  
&& make -C "/tmp/su-exec-${SU_EXEC_VERSION}" \  
&& cp "/tmp/su-exec-${SU_EXEC_VERSION}/su-exec" /usr/bin \  
&& rm -fr "/tmp/su-exec-${SU_EXEC_VERSION}" \  
&& yum autoremove -y -q gcc make \  
&& yum clean all -q \  
&& rm -fr /var/cache/yum/* /tmp/yum_save*.yumtx /root/.pki  

