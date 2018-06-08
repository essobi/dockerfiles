FROM centos:6  
MAINTAINER okazakiyuji <zaki@mbf.nifty.com>  
# ロケールの設定  
RUN localedef -f UTF-8 -i ja_JP /usr/lib/locale/ja_JP.UTF-8  
# パッケージのインストール kanon-setupのものも先にインストールする  
ADD pkglist.rhel6 /tmp/  
RUN yum -y update && \  
yum -y install mercurial `cat /tmp/pkglist.rhel6` subversion-python && \  
yum clean all  
# セットアップに必要な環境変数  
ENV KANON_IN_CONTAINER 1  
ENV MAVEN "n"  
ENV JENKINS "n"  
# マウントするフォルダの退避先を作成  
RUN mkdir -p /tmp/save  
# 上書きするファイルを/tmpにコピーする  
COPY kanon-setup /tmp/kanon-setup  
COPY pluginlist /tmp/pluginlist  
# インストール、マウントするフォルダをコピー、いらないファイルの削除  
RUN hg clone https://bitbucket.org/okamototk/kanonconductor \  
/tmp/kanonconductor && \  
cd /tmp && \  
cp kanon-setup kanonconductor/ && \  
cp pluginlist kanonconductor/ && \  
/tmp/kanonconductor/kanon-setup && \  
cd /tmp/save && \  
cp -r /var/opt/kanon ./var && \  
cp -r /etc/opt/kanon ./etc && \  
cp -r /opt/kanon/lib ./lib && \  
cd /tmp && rm -rf kanonconductor kanon-setup  
# マウントする場所を明示しておく  
VOLUME /opt/kanon/lib  
VOLUME /etc/opt/kanon  
VOLUME /var/opt/kanon  
# ホストに接続するポート  
EXPOSE 80  
# 実行時に動くスクリプトのコピー  
ADD docker-entrypoint.sh /  
# 実行時に起動するファイルの指定  
ENTRYPOINT ["/docker-entrypoint.sh"]  
# 実行時のスクリプトに渡す引数(コマンド)  
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]  

