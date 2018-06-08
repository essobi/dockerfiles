FROM fedora  
  
MAINTAINER woodruff <sansonthomas28@gmail.com>  
  
RUN dnf update -y && dnf install unzip gcc perl perl-DBI perl-CPAN tar perl-
DBD-Pg postgresql-devel perl-open -y  
  
RUN curl -L -o /tmp/ora2pg.zip
https://github.com/darold/ora2pg/archive/v17.6.zip && (cd /tmp && unzip
ora2pg.zip && rm -f ora2pg.zip) && mv /tmp/ora2pg* /tmp/ora2pg && (cd
/tmp/ora2pg && perl Makefile.PL && make && make install)  
  
RUN mkdir /usr/lib/oracle/12.1/client64/network/admin -p  
  
RUN curl -o /tmp/oraclient-basic.rpm ftp://ftp.icm.edu.pl/vol/rzm5/linux-
slc/centos/7.1.1503/cernonly/x86_64/Packages/oracle-
instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm && \  
dnf install /tmp/oraclient-basic.rpm --nogpgcheck -y && \  
rm -f /tmp/oraclient-basic.rpm && \  
curl -o /tmp/oraclient-devel.rpm ftp://ftp.icm.edu.pl/vol/rzm5/linux-
slc/centos/7.1.1503/cernonly/x86_64/Packages/oracle-
instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm && \  
dnf install /tmp/oraclient-devel.rpm --nogpgcheck -y && \  
rm -f /tmp/oraclient-devel.rpm && \  
curl -o /tmp/oraclient-sqlplus.rpm ftp://ftp.icm.edu.pl/vol/rzm5/linux-
slc/centos/7.0.1406/cernonly/x86_64/Packages/oracle-
instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm && \  
dnf install /tmp/oraclient-sqlplus.rpm --nogpgcheck -y && \  
rm -f /tmp/oraclient-sqlplus.rpm  
  
ENV ORACLE_HOME=/usr/lib/oracle/12.1/client64  
ENV TNS_ADMIN=/usr/lib/oracle/12.1/client64/network/admin  
ENV LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/oracle/12.1/client64/bin  
  
RUN curl -L http://www.perl.org/CPAN/authors/id/P/PY/PYTHIAN/DBD-
Oracle-1.74.tar.gz | (cd /tmp && tar -zxvf -) && \  
mv /tmp/DBD-Ora* /tmp/DBD-Oracle  
  
RUN cd /tmp/DBD-Oracle && perl Makefile.PL -l && make && make install  
  
RUN mkdir /data  
  
RUN ora2pg --project_base /data --init_project ora2pg-example  
  
VOLUME /data  

