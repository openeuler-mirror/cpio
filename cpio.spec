Name:           cpio
Version:        2.13
Release:        5
Summary:        A GNU archiving program

License:        GPLv3+
URL:            https://www.gnu.org/software/cpio
Source0:        https://ftp.gnu.org/gnu/cpio/%{name}-%{version}.tar.bz2

Patch0:         cpio-2.9-rh.patch
Patch1:         cpio-2.13-exitCode.patch
Patch2:         cpio-2.13-dev_number.patch
Patch3:         cpio-2.9.90-defaultremoteshell.patch
Patch4:         cpio-2.10-patternnamesigsegv.patch
Patch5:         cpio-2.10-longnames-split.patch
Patch6:         cpio-2.11-crc-fips-nit.patch
Patch7:		revert-CVE-2015-1197.patch
Patch8:         backport-0001-CVE-2021-38185-Rewrite-dynamic-string-support.patch
Patch9:         backport-0002-CVE-2021-38185-Fix-previous-commit.patch
Patch10:        backport-0003-CVE-2021-38185-Fix-dynamic-string-reallocations.patch
Patch11:        backport-CVE-2015-1197-Fix-45b0ee2b407913c533f7ded8d6f8cbeec16ff6ca.patch

Patch9000:      add-option-to-add-metadata-in-copy-out-mode.patch
Patch9001:      Fix-use-after-free-and-return-appropriate-error.patch

Provides:       bundled(gnulib)
Provides:       /bin/cpio
BuildRequires:  gcc texinfo gettext gettext-devel rmt autoconf automake

%description
GNU cpio copies files into or out of a cpio or tar archive.
The archive can be another file on the disk, a magnetic
tape, or a pipe.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -fi
%configure --with-rmt="%{_sysconfdir}/rmt"
%make_build

%install
%make_install
rm -rf %{buildroot}/usr/share/man/man8*
rm -rf %{buildroot}/usr/libexec/
rm -rf %{buildroot}/usr/share/info/dir

%check
make check

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}*
%{_datadir}/info/*.info*
%{_datadir}/locale/*/LC_MESSAGES/cpio.mo

%files help
%doc NEWS TODO THANKS
%{_datadir}/man/man1/%{name}.1.gz

%changelog
* Sat May 27 2023 fuanan <fuanan3@h-partners.com> - 2.13-5
- Type:CVE
- ID:CVE-2015-1197
- SUG:NA
- DESC:Fix CVE-2015-1197

* Tue Aug 24 2021 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 2.13-4
- Type:CVE
- ID:CVE-2021-38185
- SUG:NA
- DESC:Fix CVE-2021-38185

* Fri Jun 4 2021 fuanan <fuanan3@huawei.com> - 2.13-3
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add 'autoconf automake' to BuildRequires to use autoreconf command

* Thu Nov 26 2020 Liquor <lirui130@huawei.com> - 2.13-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:revert fix CVE-2015-1197 because it causes shutdowm problems

* Sun Aug 23 2020 chengquan <chengquan3@huawei.com> - 2.13-1
- Update software to v2.13

* Wed Aug 12 2020 Liquor <lirui130@huawei.com> - 2.12-15
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:use /etc/rmt as default rmt command

* Sat Dec 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.12-14
- Fix CVE-2019-14866

* Tue Sep 24 2019 shenyangyang<shenyangyang4@huawei.com> - 2.12-13
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:add help package

* Tue Aug 27 2019 openEuler Builteam <buildteam@openeuler.org> - 2.12-12
- Type:NA
- ID:NA
- SUG:NA
- DESC: Rewrite Spec File

* Thu Mar 21 2019 Zhipeng Xie <xiezhipeng1@huawei.com> - 2.12-11
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:modify patch name

* Fri Mar 15 2019 zhangyujing <zhangyujing1@huawei.com> - 2.12-10
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix out of bounds read
        Fix signed integer overflow big block sizes

* Thu Jul 12 2018 openEuler Builteam <buildteam@openeuler.org> - 2.12-9
- Package  Initialization

