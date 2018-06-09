#!/bin/sh  
# Copyright © (C) 2017 Emory Merryman <emory.merryman@gmail.com>  
# This file is part of git.  
#  
# git is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# git is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with git. If not, see <http://www.gnu.org/licenses/>.  
FROM emorymerryman/base:0.2.3  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
RUN \  
apk update && \  
apk upgrade && \  
apk add git && \  
true  
ENTRYPOINT ["/usr/bin/git"]  
CMD []

