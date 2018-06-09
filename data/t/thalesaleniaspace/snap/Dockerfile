#Builds a docker with SNAP based on CentOS 7  
FROM centos:7  
  
ENV \  
TBX="esa-snap_sentinel_unix_6_0.sh" \  
URL="http://step.esa.int/downloads/6.0/installers/"  
  
RUN yum -y update &&\  
yum -y install gcc gcc-c++ wget gzip which &&\  
yum clean all  
  
RUN wget $URL/$TBX && chmod +x $TBX &&\  
echo -e
"deleteAllSnapEngineDir\$Boolean=false\ndeleteOnlySnapDesktopDir\$Boolean=false\nexecuteLauncherWithPythonAction\$Boolean=false\nforcePython\$Boolean=false\npythonExecutable=/usr/bin/python\nsys.adminRights\$Boolean=true\nsys.component.RSTB\$Boolean=true\nsys.component.S1TBX\$Boolean=true\nsys.component.S2TBX\$Boolean=true\nsys.component.S3TBX\$Boolean=true\nsys.component.SNAP\$Boolean=true\nsys.installationDir=/opt/snap\nsys.languageId=en\nsys.programGroupDisabled\$Boolean=false\nsys.symlinkDir=/usr/local/bin"
>/tmp/snap.varfile &&\  
./$TBX -q -varfile /tmp/snap.varfile &&\  
rm -f $TBX  
  
COPY S1_Cal_Deb_ML_Spk_TC_cmd.xml /S1_Cal_Deb_ML_Spk_TC_cmd.xml  
COPY gpt.vmoptions /opt/snap/bin  
ENV PATH=/opt/snap/bin:$PATH  
ENV LD_LIBRARY_PATH=.  
  
#RUN snap --nosplash --nogui --modules --update-all  

