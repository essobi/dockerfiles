FROM grahamdumpleton/warp0-debian8-python27  
  
# Insert override S2I builder scripts into '.s2i' directory under the  
# application root directory. These will perform additional steps but  
# still call the original S2I scripts.  
COPY s2i ${WARPDRIVE_APP_ROOT}/.s2i  
  
# Install the Sphinx package. This will be installed in the Python  
# virtual environment under the application root directory.  
RUN pip install --no-cache 'Sphinx<1.5'  
  
# Update labels of the S2I builder to reflect that it implements a  
# generator for a Sphinx site. Leave labels related to the location of  
# the S2I scripts alone as they are still used.  
LABEL io.k8s.description="S2I builder for hosting Sphinx site." \  
io.k8s.display-name="Sphinx Server" \  
io.openshift.tags="builder,sphinx"  

