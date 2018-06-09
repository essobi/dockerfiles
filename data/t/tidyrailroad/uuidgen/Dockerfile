# Copyright © (C) 2017 Emory Merryman <emory.merryman@gmail.com>  
# This file is part of uuidgen.  
#  
# uuidgen is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# uuidgen is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with uuidgen. If not, see <http://www.gnu.org/licenses/>.  
FROM fedora:25  
MAINTAINER Emory Merryman <emory.merryman@gmail.com  
RUN \  
dnf update --assumeyes && \  
dnf install --assumeyes util-linux &&\  
dnf update --assumeyes && \  
dnf clean all  
ENTRYPOINT ["/usr/bin/uuidgen"]  
CMD []

