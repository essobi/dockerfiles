# DOCKER-VERSION 1.0  
FROM dit4c/dit4c-container-base:debian  
MAINTAINER t.dettrick@uq.edu.au  
  
# Install Python PIP  
RUN apt-get update && apt-get install -y python-pip python-dev  
  
# Install Jupyter from PIP  
RUN pip install jupyter  
  
# Based on official Julia image  
RUN export JULIA_VERSION=0.4.3 \  
&& cd /tmp \  
&& curl -sSL
"https://julialang.s3.amazonaws.com/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz"
-o julia.tar.gz \  
&& curl -sSL
"https://julialang.s3.amazonaws.com/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz.asc"
-o julia.tar.gz.asc \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
3673DF529D9049477F76B37566E3C7DC03D6E495 \  
&& gpg --batch --verify julia.tar.gz.asc julia.tar.gz \  
&& tar -xzf julia.tar.gz -C /usr/local \--strip-components 1 \  
&& rm -rf julia.tar.gz*  
  
# Create IJulia profile and required Jupyter config  
RUN su - researcher -c "julia -e 'Pkg.init(); Pkg.add(\"IJulia\")'" && \  
su - researcher -c "mkdir -p ~/.jupyter && echo \"c.NotebookApp.base_url =
'/jupyter'\" > ~/.jupyter/jupyter_notebook_config.py"  
  
# Add supporting files (directory at a time to improve build speed)  
COPY etc /etc  
COPY opt /opt  
COPY var /var  
  
# Chowned to root, so reverse that change  
RUN chown -R researcher /var/log/easydav /var/log/supervisor  
  
# Check nginx config is OK and Julia works  
RUN nginx -t && julia -v  

