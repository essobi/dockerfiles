FROM webdevops/base-app:centos-7  
MAINTAINER guillaume.camus@gmail.com  
  
LABEL vendor=infogene \  
version=1.0 \  
disclamer="Image for running Oracle Database 11g Standard/Enterprise. Due to
oracle license restrictions image is not contain database itself and will
install it on first run from external directory"  
  
RUN /usr/local/bin/yum-install \  
bindutils \  
compat-libstdc++-33 \  
compat-libstdc++-33.i686 \  
ksh \  
elfutils-libelf \  
elfutils-libelf-devel \  
glibc \  
glib-common \  
glib-devel \  
gcc \  
gcc-c++ \  
libaio \  
libaio.i686 \  
libaio-devel \  
libaio-devel.i686 \  
libgcc \  
libstdc++ \  
libstdc++.i686 \  
libstdc++-devel \  
libstdc++-devel.i686 \  
make \  
sysstat \  
unixODBC \  
unixODBC-devel \  
compat-db \  
compat-gcc-44 \  
compat-gcc-44-c++ \  
java-1.8.0-openjdk \  
unzip  
  
EXPOSE 1521  
COPY conf/ /opt/docker/  
  
ENV TMP=/tmp  
ENV ORACLE_HOSTNAME=localhost  
ENV ORACLE_UNQNAME=ORA11G  
ENV ORACLE_BASE=/data/oracle/app  
ENV ORACLE_HOME=$ORACLE_BASE/product/11.2.0/db_1  
ENV ORACLE_INVENTORY=/data/oracle/oraInventory  
ENV ORACLE_HOME_LISTENER=$ORACLE_HOME  
ENV ORACLE_SID=ORA11G  
ENV PATH=$PATH:$ORACLE_BASE/bin:$ORACLE_HOME/bin  
ENV
LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib:/usr/lib/oracle/11.2/client64/lib  
ENV CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib  
ENV NLS_LANG="FRENCH_FRANCE.WE8ISO8859P1"  
ENV NLS_NUMERIC_CHARACTERS=". "  
ENV NLS_DATE_FORMAT="YYYYMMDD"  
RUN bash /opt/docker/bin/control.sh provision.role.entrypoint oracle  
  
RUN bash /opt/docker/bin/control.sh provision.role.bootstrap oracle \  
&& bash /opt/docker/bin/bootstrap.sh  
  
VOLUME [ "/data/oracle/app", "/data/oracle/oraInventory",
"/data/oracle/dpdump"]  
  
WORKDIR /data/oracle  
  
CMD ["supervisord"]

