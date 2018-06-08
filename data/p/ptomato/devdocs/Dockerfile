  
FROM fedora  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Build dependencies and GIR packages  
RUN dnf update -y && \  
dnf install -y 'dnf-command(builddep)' git redhat-rpm-config gcc{,-c++} \  
libxml2-devel nodejs python-markdown && \  
dnf builddep -y gobject-introspection && \  
dnf install -y NetworkManager-glib-devel cairo-devel cheese-libs-devel \  
clutter-{gst,gst2,gst3,gtk}-devel evince-devel geocode-glib-devel \  
glib2-devel gnome-online-accounts-devel gobject-introspection-devel \  
gom-devel grilo-devel gsound-devel gspell-devel \  
gstreamer1-{,plugins-base-}devel gtk{2,3}-devel gtksourceview3-devel \  
gupnp-devel gupnp-dlna-devel harfbuzz-devel ibus-devel \  
keybinder3-devel libappindicator-gtk3-devel libappstream-glib-devel \  
libchamplain-devel libgudev-devel libgweather-devel libgxps-devel \  
libnotify-devel libpeas-devel librsvg2-devel libsecret-devel \  
libzapojit-devel pango-devel polkit-devel poppler-glib-devel \  
rest-devel telepathy-glib-devel tracker-devel udisks-devel \  
upower-devel vte{,291,3}-devel webkitgtk{,3,4}-devel  
  
# Get rvm in order to use the particular version of Ruby that Devdocs needs  
# bash -l starts a login shell which gets us into the rvm environment  
RUN curl -sSL https://rvm.io/mpapis.asc | gpg2 --import - && \  
curl -L https://get.rvm.io | bash -s stable && \  
/bin/bash -l -c "rvm requirements" && \  
/bin/bash -l -c "rvm install 2.4.1" && \  
/bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
  
RUN git clone https://github.com/ptomato/gobject-introspection -b
wip/ptomato/devdocs322 --depth=1 /opt/gi  
WORKDIR /opt/gi  
RUN ./autogen.sh --enable-doctool && make install  
ENV G_IR_DOC_TOOL /usr/local/bin/g-ir-doc-tool  
  
COPY lib/docs/scrapers/gnome/girs/GtkosxApplication-1.0.gir
/usr/share/gir-1.0/  
COPY . /opt/devdocs/  
WORKDIR /opt/devdocs  
RUN /bin/bash -l -c "bundle install"  
RUN /bin/bash -l -c "thor gir:generate_all /usr/share && \  
thor docs:list && \  
for docset in appindicator301 appstreamglib10 atk10 atspi20 cairo10 \  
cally10 champlain012 cheese30 clutter10 cluttergdk10 cluttergst10 \  
cluttergst20 cluttergst30 clutterx1110 cogl10 cogl20 coglpango10 \  
coglpango20 css dbusmenu04 evincedocument30 evinceview30 gcab10 gdk20 \  
gdk30 gdkpixbuf20 gdkx1120 gdkx1130 geocodeglib10 gio20 \  
girepository20 glib20 gmodule20 goa10 gobject20 gom10 grl03 grlnet03 \  
grlpls03 gsound10 gspell1 gssdp10 gst10 gstallocators10 gstapp10 \  
gstaudio10 gstbase10 gstcheck10 gstcontroller10 gstfft10 gstnet10 \  
gstpbutils10 gstrtp10 gstrtsp10 gstsdp10 gsttag10 gstvideo10 gtk20 \  
gtk30 gtkchamplain012 gtkclutter10 gtksource30 gtkosxapplication10 \  
gudev10 gupnp10 gupnpdlna20 gupnpdlnagst20 gweather30 gxps01 ibus10 \  
javascript json10 keybinder30 networkmanager10 nmclient10 notify07 \  
pango10 pangocairo10 pangoft210 pangoxft10 peas10 peasgtk10 polkit10 \  
polkitagent10 poppler018 rest07 restextras07 rsvg20 secret1 soup24 \  
soupgnome24 telepathyglib012 tracker10 trackercontrol10 trackerminer10 \  
upowerglib10 vte00 vte290 vte291 webkit10 webkit30 webkit240 \  
webkit2webextension40 zpj00; \  
do echo \$docset; thor docs:generate \$docset --force; done"  
  
EXPOSE 9292  
CMD /bin/bash -l -c "rackup -o 0.0.0.0"  
  

