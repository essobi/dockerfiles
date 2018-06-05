# Copyright (C) Sam Parkinson 2014  
#  
# This file is part of ASLO.  
#  
# ASLO is free software: you can redistribute it and/or modify it under  
# the terms of the GNU Affero General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# ASLO is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU Affero General Public License for more details.  
#  
# You should have received a copy of the GNU Affero General Public License  
# along with ASLO. If not, see <http://www.gnu.org/licenses/>.  
  
FROM fedora:21  
# Install Deps  
RUN yum install -y \  
sugar-toolkit-gtk3 \  
patch  
  
# Patch to add the --no-fail option  
RUN curl -O https://patch-diff.githubusercontent.com/raw/sugarlabs/sugar-
toolkit-gtk3/pull/169.patch; \  
patch /usr/lib/python2.7/site-packages/sugar3/activity/bundlebuilder.py  
< 169.patch; \  
rm 169.patch  
  
# Sugar lib (gtk2) dosn't seem to install properly  
# So we add a link that makes it sugar3  
RUN rm -rf /usr/lib/python2.7/site-packages/sugar  
RUN ln -s /usr/lib/python2.7/site-packages/sugar3 /usr/lib/python2.7/site-
packages/sugar  
  
RUN mkdir /activity  
VOLUME /activity  
  
WORKDIR /activity  
ENTRYPOINT ["sh", "-c", "python setup.py dist_xo --no-fail; chmod 777
/activity/*; rm -rf /activity/locale"]  

