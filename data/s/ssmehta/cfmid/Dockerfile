FROM ssmehta/rdkit:Release_2016_03_1  
MAINTAINER Sajjan Singh Mehta "sajjan.s.mehta@gmail.com"  
# Set home directory  
ENV HOME /root  
WORKDIR /root  
  
# Download dependencies  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y subversion libboost-filesystem-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Add sources  
ADD
http://downloads.sourceforge.net/project/lpsolve/lpsolve/5.5.2.0/lp_solve_5.5.2.0_source.tar.gz
/root/  
RUN tar xzvf lp_solve_5.5.2.0_source.tar.gz && \  
rm lp_solve_5.5.2.0_source.tar.gz  
  
# Compile LPSolve  
RUN chmod +x /root/lp_solve_5.5/lpsolve55/ccc  
RUN cd /root/lp_solve_5.5/lpsolve55 && \  
./ccc  
  
# Compile CFM-ID  
RUN svn checkout -r 25 svn://svn.code.sf.net/p/cfm-id/code/ cfm-id-code  
  
RUN ls -l /root/lp_solve_5.5/lpsolve55/bin/ux64 && \  
mkdir /root/cfm-id-code/cfm/build && \  
cd /root/cfm-id-code/cfm/build && \  
cmake .. -DLPSOLVE_INCLUDE_DIR=/root/lp_solve_5.5
-DLPSOLVE_LIBRARY_DIR=/root/lp_solve_5.5/lpsolve55/bin/ux64 && \  
make install  
  
# Set environmental variables  
ENV LD_LIBRARY_PATH
$LD_LIBRARY_PATH:$RDBASE/lib:/root/lp_solve_5.5/lpsolve55/bin/ux64  
ENV PATH $PATH:/root/cfm-id-code/cfm/bin  
  
# Set entrypoint  
ENTRYPOINT ["./docker_entrypoint.sh"]  

