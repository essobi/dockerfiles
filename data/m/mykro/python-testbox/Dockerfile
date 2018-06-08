# Python-testbox  
# Copyright (C) 2016 Mykro Enterprises New Zealand Limited  
# Author: Matthew Hartstonge  
# E-mail: <matt@mykro.co.nz>  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
FROM ubuntu:wily  
MAINTAINER Matthew Hartstonge <matt@mykro.co.nz>  
  
RUN groupadd -r test_user && useradd -r -g test_user test_user  
RUN apt-get update && apt-get install -y software-properties-common \  
&& apt-add-repository -y ppa:fkrull/deadsnakes \  
&& apt-add-repository -y ppa:pypy/ppa \  
&& apt-get update && apt-get install -y git \  
python \  
python-pip \  
pypy \  
python2.3 \  
python2.4 \  
python2.5 \  
python2.6 \  
# 2.7 provided by wily  
python3.1 \  
python3.2 \  
python3.3 \  
&& pip install coverage nose tox pytest pytest-cov \  
&& apt-get purge -y --auto-remove software-properties-common \  
&& rm -rf /var/lib/apt/lists/*  

