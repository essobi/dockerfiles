FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y wget unzip samtools rsync  
WORKDIR /root  
RUN wget
https://downloads.pacbcloud.com/public/software/installers/smrtlink_5.0.1.9585.zip  
RUN unzip -o -P nX4dmaR% smrtlink_5.0.1.9585.zip  
RUN sh smrtlink_5.0.1.9585.run --rootdir smrtlink --smrttools-only  
RUN rm -f smrtlink_5.0.1.9585.zip smrtlink_5.0.1.9585.run*  
ENV
PATH=/root/smrtlink/smrtcmds/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
RUN apt-get update && apt-get install -y git python  
RUN git clone \--recursive git://github.com/vetscience/Tools  
#RUN git clone -b '1.0.4-beta' --single-branch --depth 1
https://github.com/vetscience/Tools  
WORKDIR /root/Tools  
RUN chmod uog+x /root && chmod uog+rwx /root/Tools && chmod uog+x
/root/Tools/Assembly && chmod uog+x /root/Tools/Assembly/createFofn.py  
RUN cp Cwl/arrow/smrtpipe.sh . && cp Cwl/arrow/preset.xml .  
RUN chmod uog+x smrtpipe.sh && chmod uog+rwx preset.xml  
ENV PYTHONPATH=/root/Tools  
RUN mv /root/smrtlink/install/smrtlink-
release_5.0.1.9585/bundles/smrttools/install/smrttools-
release_5.0.1.9578/private/pacbio/pythonpkgs/pbcore/lib/python2.7/site-
packages/pbcore/data/datasets /root/smrtlink/  
RUN ln -s /var/spool/cwl/datasets /root/smrtlink/install/smrtlink-
release_5.0.1.9585/bundles/smrttools/install/smrttools-
release_5.0.1.9578/private/pacbio/pythonpkgs/pbcore/lib/python2.7/site-
packages/pbcore/data/datasets  
ENTRYPOINT ["/root/Tools/smrtpipe.sh"]  

