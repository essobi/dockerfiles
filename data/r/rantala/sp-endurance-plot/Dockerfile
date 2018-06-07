# Docker image with endurance-plot and dependencies installed.  
FROM docker.io/fedora  
RUN dnf -y update && dnf clean all  
RUN dnf -y install \  
gcc \  
gnuplot \  
make \  
netpbm-progs \  
perl \  
perl-Inline-C \  
perl-JSON \  
perl-List-MoreUtils \  
perl-Parallel-ForkManager \  
perl-Tie-IxHash \  
redhat-rpm-config \  
&& dnf clean all  
COPY . sp-endurance  
RUN make -C sp-endurance \  
postproc-lib \  
install-postproc-lib \  
install-postproc \  
&& rm -rf sp-endurance  
CMD if [ -e /data ] ; then\  
cd /data || exit $?;\  
DIRS=$(ls -1 | grep -E ^[0-9]+);\  
if [ -z "$DIRS" ] ; then\  
echo 2>&1 "ERROR: \  
unable to find any endurance-snapshot data directory (example: 000, 001,
...)";\  
exit 1;\  
fi;\  
endurance-plot -j $(nproc) $DIRS; exit $?;\  
else\  
printf "USAGE:\n\  
To generate graphs, share your data collected with endurance-snapshot into\n\  
the container /data directory.\n\  
\n\  
The graphs and HTML are generated into the same directory.\n\  
\n\  
Example:\n\  
cd /path/to/files (that contains directories 000, 001, 002, ...)\n\  
docker run --rm --volume \$PWD:/data:z rantala/sp-endurance-plot\n\n";\  
fi  

