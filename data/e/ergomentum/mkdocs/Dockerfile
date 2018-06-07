FROM centos:7.4.1708 as builder  
ENV LANG='C' LANGUAGE='C' LC_ALL='C'  
COPY yum.conf /etc  
RUN mkdir -p /target  
RUN yum --installroot=/target --releasever=/ install python python-setuptools
git  
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
RUN python get-pip.py  
RUN pip install --install-option="--prefix=/target" mkdocs  
RUN rm -rf /target/usr/share/{man,doc,info,gnome/help} /target/var/cache/yum  
RUN cp -a {,/target}/etc/yum.conf  
RUN localedef --prefix=/target --list-archive|xargs localedef --prefix=/target
--delete-from-archive  
RUN mv /target/usr/lib/locale/locale-archive{,.tmpl}  
RUN chroot /target build-locale-archive  
RUN sed -E 's/(.*)127.0.0.1(.*)/\10.0.0.0\2/' -i
/target/usr/lib/python2.7/site-packages/mkdocs/config/defaults.py  
RUN mkdir /target/root/.ssh/  
FROM scratch  
ENV LANG='C' LANGUAGE='C' LC_ALL='C'  
COPY \--from=builder /target .  
WORKDIR /mnt  
VOLUME ["/mnt"]  
ENTRYPOINT ["mkdocs"]  

