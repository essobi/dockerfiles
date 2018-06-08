# Use the latest official Python 3.6 image as base.  
# (This uses the Debian Stretch variant so that 3.5 is also included.)  
FROM python:3.6-stretch  
  
  
# Install node.js LTS (6.x) and npm.  
#  
# XXX: https://curlpipesh.tumblr.com/  
#  
RUN curl -sSL https://deb.nodesource.com/setup_6.x | bash && apt-get install
-y nodejs  
  
# Pre-install system dependencies  
ENV DEPS_SPATIALITE libgeos-dev libgeos++-dev libproj-dev libgdal-dev sqlite3
spatialite-bin  
  
RUN apt-get update && apt-get install -y \  
${DEPS_SPATIALITE} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g \  
bower \  
# This Debian image lacks a phantomjs package,  
# so use phantomjs-prebuilt from npm instead.  
phantomjs-prebuilt \  
# Clean up after the phantomjs-prebuilt install.  
&& rm -rf /tmp/phantomjs \  
&& npm cache clean \  
# XXX: For some reason these temporary files get left behind too?  
&& rm -rf /tmp/npm-*  
  
# Add this to make --allow-root the default for bower install,  
# and prevent ESUDO errors.  
ADD .bowerrc /root/.bowerrc  
  
# Make sure pip and friends are up to date  
# XXX: Avoid 36.0.0 due to https://github.com/pypa/setuptools/issues/1042  
RUN pip install --no-cache-dir -U pip 'setuptools !=36.0.0' wheel  
  
# Python tools: Tox, flake8, MyPy  
RUN pip install --no-cache-dir -U tox flake8 mypy  
  
# XXX: Temporarily work around setuptools
https://github.com/pypa/setuptools/issues/1042  
RUN pip install --no-cache-dir -U tox-virtualenv-no-download  

