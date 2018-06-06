FROM cismet/cids-distribution:5.0  
MAINTAINER Pascal Dihé <pascal.dihe@cismet.de>  
  
LABEL de.cismet.cids.distribution.scaffold.name="cids-distribution-scaffold
image" \  
de.cismet.cids.distribution.scaffold.version="4.1-SNAPSHOT" \  
de.cismet.cids.distribution.scaffold.tag.docker="4.1-SNAPSHOT" \  
de.cismet.cids.distribution.scaffold.tag.git="cidsDistributionScaffold-4.1-SNAPSHOT"
\  
de.cismet.cids.distribution.scaffold.descripton="Scaffold cids distribution
Runtime Image"  
  
# use empty account extension -> lib/local and lib/starter  
ENV CIDS_ACCOUNT_EXTENSION=""  
ENV CIDS_LOCAL_DIR ${CIDS_LIB_DIR}/local${CIDS_ACCOUNT_EXTENSION}  
ENV CIDS_STARTER_DIR ${CIDS_LIB_DIR}/starter${CIDS_ACCOUNT_EXTENSION}  
  
# use .dockerignore to control which files go into the image and which not
(faster!)  
COPY cidsDistribution ${CIDS_DISTRIBUTION_DIR}/  
  
# expose cids-server port  
EXPOSE 9986  
# expose cids-server-rest port  
EXPOSE 8890  
# expose ngnix port  
EXPOSE 80  
#ENTRYPOINT /bin/bash

