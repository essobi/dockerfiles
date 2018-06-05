# scitran/qa_report_fmri  
#  
# Use modified CNI/NIMS code from @rfdougherty to create a qa_report for a
given fmri NIfTI file in Flywheel spec.  
# See https://github.com/cni/nims/blob/master/nimsproc/qa_report.py for
original source code.  
#  
# Example usage:  
# docker run --rm -ti \  
# -v /path/nifti_file:/flywheel/v0/input \  
# -v /path/for/output/files:/flywheel/v0/output  
# scitran/qa-report-fmri /flywheel/v0/input -i nifti_file.nii.gz  
#  
FROM scitran/qa-report-fmri:v0  
  
MAINTAINER Michael Perry <lmperry@stanford.edu>  
  
# Trigger build of font cache  
RUN python -c "from matplotlib import font_manager"  
  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
# Put the python code in place  
COPY qa-report-fmri.py ${FLYWHEEL}/qa_report.py  
  
ENTRYPOINT ["/flywheel/v0/run"]  

