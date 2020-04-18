Name:           steinway-d-274-soundfont
Version:        7.4
Release:        1%{?dist}
Summary:        Steinway D-274 piano SFZ soundfont

License:        CC-BY-SA
URL:            https://github.com/KaleidonKep99/Steinway-D-274

# Rebuild source commands:
# VERSION=$(grep ^Version *.spec | cut -d' ' -f9)
# grep "^#    " *.spec | sed 's|#    ||' | sed "s|VERSION|$VERSION|g" | bash

# Rebuild source script:
#    wget https://github.com/KaleidonKep99/Steinway-D-274/archive/VERSION.tar.gz
#    tar xf VERSION.tar.gz
#    for f in Steinway-D-274-VERSION/*.rar; do unar -o Steinway-D-274-VERSION -f $f; done
#    rm Steinway-D-274-VERSION/*.rar
#    mv Steinway-D-274-VERSION steinway-d-274-soundfont-VERSION
#    tar cvjf steinway-d-274-soundfont-VERSION.tar.gz steinway-d-274-soundfont-VERSION

Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Steinway D-274 piano KSP (Keyboard Stereo Panning) SFZ soundfont.

%prep
%autosetup

%build
sed -i 's|^default_path=..|default_path=.|' KSP-Reborn/Presets/*.sfz

%install
rm -rf $RPM_BUILD_ROOT

install -d %{buildroot}%{_datadir}/soundfonts/steinway-d-274
cp KSP-Reborn/Presets/*.sfz %{buildroot}%{_datadir}/soundfonts/steinway-d-274/
cp -r KSP-Reborn/Samples %{buildroot}%{_datadir}/soundfonts/steinway-d-274/

%files
%license "Creative Commons BY 4.0.txt"
%doc README.md "Readme, important.txt"
%{_datadir}/soundfonts/steinway-d-274

%changelog
* Sat Apr 18 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 7.4-1
- Initial build
