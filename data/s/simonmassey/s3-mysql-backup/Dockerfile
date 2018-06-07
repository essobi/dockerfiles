FROM registry.access.redhat.com/rhscl/mysql-57-rhel7  
MAINTAINER Simon Massey <simbo1905@60hertz.com>  
LABEL io.k8s.description="MySQL s3 backups" \  
io.k8s.display-name="MySQL s3 backups" \  
io.openshift.expose-services="8000:http" \  
io.openshift.tags="mysql,s3,backups"  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" && \  
unzip awscli-bundle.zip && \  
./awscli-bundle/install -b ~/bin/aws && \  
rm awscli-bundle.zip  
ENV PATH="~/bin:${PATH}"  
COPY s3mysqlbackup.sh /var/lib/mysql/bin/  
RUN mkdir -p /var/lib/mysql/.aws && chgrp root /var/lib/mysql/.aws && chmod
g+rwx /var/lib/mysql/.aws  
USER 1001  
CMD /bin/bash

