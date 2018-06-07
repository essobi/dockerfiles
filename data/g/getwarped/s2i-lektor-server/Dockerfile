FROM grahamdumpleton/warp0-debian8-python27  
  
# Insert override S2I builder scripts into '.s2i' directory under the  
# application root directory. These will perform additional steps but  
# still call the original S2I scripts.  
COPY s2i ${WARPDRIVE_APP_ROOT}/.s2i  
  
# Install the Lektor package. This will be installed in the Python  
# virtual environment under the application root directory. We do not  
# disable caching as we normally would do as when Lektor is run to do  
# the build it attempts to install packages again. By caching we avoid  
# it needing to go out and grab packages again that have already been  
# downloaded.  
RUN pip install 'Lektor<2.4'  
  
# Update labels of the S2I builder to reflect that it implements a  
# generator for a Lektor site. Leave labels related to the location of  
# the S2I scripts alone as they are still used.  
LABEL io.k8s.description="S2I builder for hosting Lektor site." \  
io.k8s.display-name="Lektor Server" \  
io.openshift.tags="builder,lektor"  

