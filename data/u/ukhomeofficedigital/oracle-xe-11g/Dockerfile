FROM centos:6  
ENV ORACLE_HOME /u01/app/oracle/product/11.2.0/xe  
ENV PATH $ORACLE_HOME/bin:$PATH  
ENV ORACLE_SID=XE  
  
EXPOSE 1521  
EXPOSE 8080  
ENV processes 500  
ENV sessions 555  
ENV transactions 610  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
RUN mkdir /build  
RUN rpm --rebuilddb && yum -y install unzip bc && yum clean all  
COPY *.ora /  
RUN groupadd dba  
RUN useradd -G dba oracle  
  
ONBUILD WORKDIR /build  
ONBUILD COPY docker_files/oracle-xe-11*.zip /build/  
ONBUILD RUN unzip oracle-xe-11*.zip  
ONBUILD WORKDIR /build/Disk1  
ONBUILD RUN rpm --rebuilddb && (yum deplist *.rpm | awk '/provider/ {print
$2}' | sort -u | xargs yum -y install) && yum clean all  
ONBUILD RUN rpm --rebuilddb && rpm -i --noscripts *.rpm  
ONBUILD RUN rpm -qp --scripts *.rpm > postinstall.sh  
ONBUILD RUN sed -i -e '1,/^postinstall scriptlet/ d' -e '/^[a-z][a-z]*
scriptlet/,$ d' postinstall.sh  
ONBUILD RUN bash postinstall.sh  
ONBUILD WORKDIR /  
ONBUILD RUN rm -rf /build  
  
ONBUILD RUN mv /init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts  
ONBUILD RUN mv /initXETemp.ora
/u01/app/oracle/product/11.2.0/xe/config/scripts  
  
ONBUILD RUN mv /u01/app/oracle/product /u01/app/oracle-product  
ONBUILD RUN chown -R oracle:dba /u01/app/oracle  
ONBUILD VOLUME ["/u01/app/oracle"]  
  

