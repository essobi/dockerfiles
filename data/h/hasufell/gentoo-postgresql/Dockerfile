FROM hasufell/gentoo-amd64-paludis:latest  
MAINTAINER Julian Ospald <hasufell@gentoo.org>  
  
##### PACKAGE INSTALLATION #####  
# copy paludis config  
COPY ./config/paludis /etc/paludis  
  
# update world with our USE flags  
RUN chgrp paludisbuild /dev/tty && cave resolve -c world -x  
  
# install tools set  
RUN chgrp paludisbuild /dev/tty && cave resolve -c tools -x  
  
# install postgresql  
ENV POSTGRES_VER 9.4  
RUN chgrp paludisbuild /dev/tty && \  
cave resolve -z dev-db/postgresql:${POSTGRES_VER} -x  
RUN chgrp paludisbuild /dev/tty && correct=true cave config dev-db/postgresql  
  
# update etc files... hope this doesn't screw up  
RUN etc-update --automode -5  
  
################################  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo -e "\nhost all all 0.0.0.0/0 md5" \  
>> /etc/postgresql-${POSTGRES_VER}/pg_hba.conf  
RUN echo -e "\nlisten_addresses='*'" \  
>> /etc/postgresql-${POSTGRES_VER}/postgresql.conf  
  
COPY modify_postgres_pass.sh /modify_postgres_pass.sh  
COPY run.sh /run.sh  
RUN mkdir /run/postgresql/ && chown postgres /run/postgresql && \  
mkdir /var/log/postgresql && chown postgres /var/log/postgresql  
RUN chmod 755 /*.sh  
  
# this allows our start script to sync the initialized db  
# if the user mounts in from the host instead of using volume data containers  
RUN cp -a /var/lib/postgresql /var/lib/postgresql-orig  
  
EXPOSE 5432  
CMD ["/run.sh"]  

