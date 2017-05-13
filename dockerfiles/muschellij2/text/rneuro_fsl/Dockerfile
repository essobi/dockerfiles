### RNEURO with FSL
FROM muschellij2/rneuro

RUN wget -O- http://neuro.debian.net/lists/wily.us-tn.full | tee /etc/apt/sources.list.d/neurodebian.sources.list \
 && apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9

RUN apt-get update \
    && apt-get install -y fsl-complete

ENV FSLDIR=/usr/local/fsl
ENV FSLSHARE=/usr/share/data
ENV PATH=$PATH:${FSLDIR}/bin

RUN mkdir -p ${FSLDIR}/bin  \
&& cp /usr/lib/fsl/5.0/* ${FSLDIR}/bin/

RUN mkdir -p ${FSLDIR}/data/standard \
&& mkdir -p ${FSLDIR}/data/atlases 

# && mkdir -p ${FSLDIR}/data/possum \
# && mkdir -p ${FSLDIR}/data/first \
#######################################
# Setting things up like other installers
#######################################
# setting up standard
RUN cp -R ${FSLSHARE}/fsl-mni152-templates/* ${FSLDIR}/data/standard/

# setting up atlases
RUN \
cp -R ${FSLSHARE}/harvard-oxford-atlases/* ${FSLDIR}/data/atlases/ \
&& cp -R ${FSLSHARE}/juelich-histological-atlas/* ${FSLDIR}/data/atlases/ \
&& cp -R ${FSLSHARE}/bangor-cerebellar-atlas/* ${FSLDIR}/data/atlases/ \
&& cp -R ${FSLSHARE}/jhu-dti-whitematter-atlas/* ${FSLDIR}/data/atlases/ \
&& cp -R ${FSLSHARE}/forstmann-subthalamic-nucleus-atlas/* ${FSLDIR}/data/atlases/ \
&& cp -R ${FSLSHARE}/fsl-resting-connectivity-parcellation-atlases/* ${FSLDIR}/data/atlases/ \
&& cp -R ${FSLSHARE}/mni-structural-atlas/* ${FSLDIR}/data/atlases/ \
&& cp -R ${FSLSHARE}/oxford-thalamic-connectivity-atlas/* ${FSLDIR}/data/atlases/ \
&& cp -R ${FSLSHARE}/talairach-daemon-atlas/* ${FSLDIR}/data/atlases/ 

ENV FSLOUTPUTTYPE=NIFTI_GZ

RUN usermod -u 504 docker

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/fsl/5.0
CMD ["bash"]

