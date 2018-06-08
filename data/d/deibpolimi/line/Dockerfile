FROM ubuntu:14.04  
MAINTAINER Riccardo B. Desantis <riccardobenito.desantis@polimi.it>  
  
# Setting the environment  
ENV JAVA_HOME /usr/lib/jvm/default-java  
ENV USERHOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER root  
  
# Update the repos and install all the used packages  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
unzip \  
xorg \  
curl && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Installing MCR  
WORKDIR /tmp  
RUN curl -L
http://it.mathworks.com/supportfiles/downloads/R2015a/deployment_files/R2015a/installers/glnxa64/MCR_R2015a_glnxa64_installer.zip
--create-dirs -o MCR/MCR_R2015a_glnxa64_installer.zip  
#COPY MCR_R2015a_glnxa64_installer.zip MCR/  
WORKDIR MCR  
RUN unzip -q MCR_R2015a_glnxa64_installer.zip && \  
./install -mode silent -agreeToLicense yes && \  
rm -rf /tmp/MCR  
  
# Installing LINE  
WORKDIR /opt  
RUN curl -OL http://svn.code.sf.net/p/line-
solver/code/branches/unstable/v072/bin/linux/LINE_072_linux.zip  
#COPY LINE_072_linux.zip ./  
RUN unzip -q LINE_072_linux.zip && \  
mv LINE_072_linux/bin LINE && \  
rm -rf LINE_072_linux*  
WORKDIR LINE  
  
# Fix the files  
RUN printf "%b\n"
"port=5463\nmaxIter=500\nmaxJobSize=6\nverbose=0\nparallel=PARFOR\ntimeoutConnection=3600\nrespTimePerc=SEFF\nrespTimePercMin=0.85\nrespTimePercStep=0.05\nrespTimePercMax=0.90\ndirectory=/opt/LINE\nsolver=FLUID"
> LINE.properties && \  
sed 's|<value>[0-9]*.0</value>|<value>4.0</value>|'
<lineClusterProfile.settings >lineClusterProfile-new.settings && \  
mv lineClusterProfile-new.settings lineClusterProfile.settings && \  
mv LINE LINE-orig && \  
printf "%b\n" '#!'"`which env`
sh\n\nMCRROOT=\"/usr/local/MATLAB/MATLAB_Runtime/v85\"\nLINEROOT=\"/opt/LINE\"\n\ncd
\${LINEROOT} && sh run_LINE.sh \${MCRROOT} \"\$@\"" > LINE && \  
sed 's|LINE|LINE-orig|' <run_LINE.sh >run_LINE-new.sh && \  
mv run_LINE-new.sh run_LINE.sh && \  
printf "%b\n" '#!'"`which sh`\n\nwhile true\ndo\n\t/opt/LINE/LINE
/opt/LINE/LINE.properties\n\tsleep 2\ndone" > run_LINE_loop.sh && \  
chmod +x run_LINE.sh LINE run_LINE_loop.sh LINE-orig  
  
## Starts LINE  
EXPOSE 5463  
CMD /opt/LINE/run_LINE_loop.sh  

