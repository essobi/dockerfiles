# this docker file is used to build a base dev env for chinese  
FROM frankshi/base_env_chinese  
MAINTAINER frank "songyangshi@gmail.com"  
ENV JAVA_VERSION 8u92  
ENV DISPLAY :1  
ENV NO_VNC_HOME /root/noVNC  
ENV VNC_COL_DEPTH 24  
ENV VNC_RESOLUTION 1280x1024  
ENV VNC_PW ssy123456  
ENV SAKULI_DOWNLOAD_URL https://labs.consol.de/sakuli/install  
ENV DIR_DEV /root/eclipse  
ENV URL_ECLIPSE
http://mirror.rise.ph/eclipse/technology/epp/downloads/release/neon/2/eclipse-
cpp-neon-2-linux-gtk-x86_64.tar.gz  
ENV URL_NO_VNC
https://raw.githubusercontent.com/shisongyang/novnc_res/master/noVNC-0.6.1.tar.gz  
ENV URL_WEB_SOKIFY
https://raw.githubusercontent.com/shisongyang/novnc_res/master/websockify-0.8.0.tar.gz  
ENV URL_CPP_REF
http://upload.cppreference.com/mwiki/images/f/f2/html_book_20170214.tar.gz  
ENV DIR_IBUS /root/.config/dconf  
ENV DIR_CPP_REF /root/cpp_ref  
ENV URL_GOOGLE_CHROME https://dl.google.com/linux/direct/google-chrome-
stable_current_x86_64.rpm  
  
  
# vnc xfce  
RUN yum --enablerepo=epel -y -x gnome-keyring --skip-broken groups install
"Xfce" \  
&& yum -y install tigervnc-server && yum -y install gedit && yum clean all -y  
  
# novnc  
RUN mkdir -p $NO_VNC_HOME/utils/websockify \  
&& wget -qO- $URL_NO_VNC | tar xz --strip 1 -C $NO_VNC_HOME \  
&& wget -qO- $URL_WEB_SOKIFY | tar xz --strip 1 -C
$NO_VNC_HOME/utils/websockify \  
&& chmod +x -v /root/noVNC/utils/*.sh  
  
# java  
RUN yum -y install $SAKULI_DOWNLOAD_URL/3rd-party/java/jre-$JAVA_VERSION-
linux-x64.rpm && yum clean all  
  
# xvnc server porst, if $DISPLAY=:1 port will be 5901  
EXPOSE 5901  
# novnc web port  
EXPOSE 6901  
ADD .vnc /root/.vnc  
ADD .config /root/.config  
ADD scripts /root/scripts  
  
# config Disable xfce-polkit  
RUN chmod +x /root/scripts/*.sh /root/.vnc/xstartup /etc/xdg/xfce4/xinitrc \  
&& /bin/dbus-uuidgen > /etc/machine-id \  
&& rm /etc/xdg/autostart/xfce-polkit.desktop  
  
# chinese input  
RUN yum -y install ibus ibus-libpinyin ibus-qt ibus-table-chinese-array im-
chooser && yum clean all -y  
  
# cpp reference browser and pdf reader ibus setup  
RUN mkdir -p $DIR_CPP_REF \  
&& wget -qO- $URL_CPP_REF | tar xz --strip 1 -C $DIR_CPP_REF \  
&& mkdir -p $DIR_IBUS \  
&& yum -y install evince goldendict cppcheck \  
&& wget $URL_GOOGLE_CHROME \  
&& yum -y install google-chrome-stable_current_x86_64.rpm \  
&& rm -rf /etc/yum.repos.d/google-chrome.repo \  
&& yum clean all -y  
  
ADD def_res /root/def_res  
COPY def_setup/ibus/user $DIR_IBUS  
ADD def_setup/goldendict.tar.gz /root/  
ADD def_setup/eclipse_config.tar.gz /root/  
ADD def_setup/sublime.tar.gz /root/  
COPY def_setup/eclipse_workspace.tar.gz /root/  
COPY def_setup/Bookmarks /root/.config/google-chrome/Default/  
COPY def_setup/google-chrome /usr/bin/  
COPY def_setup/ansible.cfg /etc/ansible/  
COPY def_setup/.bashrc /root/  
  
# eclipse  
#RUN mkdir -p $DIR_DEV \  
# && wget -qO- $URL_ECLIPSE | tar xz --strip 1 -C $DIR_DEV  
RUN cat /root/def_res/eclipse/* > /root/eclipse.tar.gz && rm -rf
/root/def_res/eclipse/ \  
&& tar -zxf /root/eclipse.tar.gz -C /root/ && rm -f /root/eclipse.tar.gz  
  
ENV GRPC_RELEASE_TAG v1.4.0  
RUN git clone -b ${GRPC_RELEASE_TAG} https://github.com/grpc/grpc
/var/local/git/grpc  
  
# install grpc  
RUN cd /var/local/git/grpc && \  
git submodule update --init && \  
make && \  
make install && make clean  
#install protoc  
RUN cd /var/local/git/grpc/third_party/protobuf && \  
make && make install && make clean  
  
# install atom  
ENTRYPOINT ["/root/scripts/vnc_startup.sh"]  
CMD ["--tail-log"]  
  

