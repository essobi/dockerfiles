###########################################################  
# VikingCo: Kong Admin  
###########################################################  
FROM vikingco/django:3.4  
MAINTAINER Dirk Moors  
  
# Override DJANGOROOT  
ENV DJANGOROOT ${SRCDIR}/app  
  
# Override WSGIFILE (Relative to DJANGOROOT)  
ENV WSGIFILE admin/wsgi.py  
  
# override settings file  
ENV DJANGO_SETTINGS_MODULE admin.settings.local  
  
# Add deployment dir  
ADD deployment ${DEPLOYMENTDIR}  
  
# install and configure packages  
RUN set -v \  
&& buildDeps=`cat ${DEPLOYMENTDIR}/${BUILDDEPSFILE}` && echo $buildDeps \  
&& requiredAptPackages=`cat ${DEPLOYMENTDIR}/${DEPSFILE}` && echo
requiredAptPackages \  
&& apt-get update \  
&& apt-get install -y $buildDeps $requiredAptPackages --no-install-recommends
\  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install -U pip \  
&& pip install -r ${DEPLOYMENTDIR}/requirements.txt \  
&& pip freeze \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' + \  
&& apt-get purge -y --auto-remove $buildDeps  
  
# Copy source  
COPY . ${SRCDIR}  
  
# Change workdir  
WORKDIR ${DJANGOROOT}  

