FROM python:2.7.11  
RUN pip install rdflib prov nibabel numpy nidmresults  
RUN git clone https://github.com/incf-nidash/nidmresults-fsl.git  
RUN cd nidmresults-fsl && python setup.py install  
ENV FSLOUTPUTTYPE NIFTI_GZ  
ADD smoothest /usr/bin/  

