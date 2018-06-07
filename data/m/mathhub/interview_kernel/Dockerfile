ARG DOCKER_NOTEBOOK_IMAGE=jupyter/minimal-notebook:e1677043235c  
FROM $DOCKER_NOTEBOOK_IMAGE  
ARG JUPYTERHUB_VERSION=0.8.0  
ADD interview_kernel mmt_interview_kernel/interview_kernel  
ADD setup.py mmt_interview_kernel/setup.py  
ADD README.md mmt_interview_kernel/README.md  
ADD example_notebook.ipynb example_notebook.ipynb  
  
USER root  
RUN apt-get update && apt-get install -y openjdk-8-jre-headless && apt-get
clean  
RUN python3 -m pip install --no-cache jupyterhub==$JUPYTERHUB_VERSION \  
&& cd mmt_interview_kernel \  
&& pip install . \  
&& python3 -m interview_kernel.install \  
&& cd ../ && rm -rf mmt_interview_kernel \  
&& git clone https://github.com/kwarc/jupyter-console-standalone \  
&& cd jupyter-console-standalone/jcs/files && npm install && npm run build &&
cd ../../ \  
&& python setup.py install && jupyter serverextension enable \--sys-prefix
--py jcs && cd .. \  
&& rm -rf jupyter-console-standalone \  

